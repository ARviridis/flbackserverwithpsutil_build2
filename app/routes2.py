# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, request
from app import app
from app.database import device, db, conn
from app.forms import dev
@app.route('/req', methods=['GET', 'POST'])
def req():  # if current_user.is_authenticated:
    db.execute("select sectors.id_noms,sectors.object1, sectors.object2, sectors.object3,sectors.object4,sectors.object5 from sectors")
    dv1 = db.fetchall()  # все девайсы
    dvmy = dv1  # просто обЪявление dvmy
    dvmypoisk = dv1
    form = dev()
    if form.ppb.data == True:#search
        if form.object1.data == '':
            if form.object2.data == '':
                if form.object3.data == '':
                    if form.object4.data == '':
                        flash('poisk')
                        return render_template('req.html', title='devices', form=form, dv=dv1, dvmy=dvmy,
                                               dvmypoisk=dvmypoisk, )
                    else:
                        db.execute(
                            "select sectors.id_noms,sectors.object1, sectors.object2, sectors.object3, sectors.object4,sectors.object5 from sectors where (sectors.object4 = ?);",
                            (form.object4.data,))
                        dvmypoisk = db.fetchall()
                        device.rr = form.object4.data  # для фильтрации!!!!!!!!!!!!!
                        if dvmypoisk == []:
                            flash(device.rr)
                            return render_template('req.html', title='devices', form=form, dv=dv1, dvmy=dvmy,
                                                   dvmypoisk=dvmypoisk, )
                else:
                    db.execute(
                        "select sectors.id_noms,sectors.object1, sectors.object2, sectors.object3, sectors.object4,sectors.object5 from sectors where (sectors.object3 = ?);",
                        (form.object3.data,))
                    dvmypoisk = db.fetchall()
                    device.rr = form.object3.data  # для фильтрации!!!!!!!!!!!!!
                    if dvmypoisk == []:
                        flash(device.rr)
                        return render_template('req.html', title='devices', form=form, dv=dv1, dvmy=dvmy,
                                               dvmypoisk=dvmypoisk, )
            else:
                db.execute(
                    "select sectors.id_noms,sectors.object1, sectors.object2, sectors.object3, sectors.object4,sectors.object5 from sectors where (sectors.object2 = ?);",
                    (form.object2.data,))
                dvmypoisk = db.fetchall()
                device.rr = form.object2.data  # для фильтрации!!!!!!!!!!!!!
                if dvmypoisk == []:
                    flash(device.rr)
                    return render_template('req.html', title='devices', form=form, dv=dv1, dvmy=dvmy,
                                           dvmypoisk=dvmypoisk, )
        else:
            db.execute("select sectors.id_noms,sectors.object1, sectors.object2, sectors.object3, sectors.object4,sectors.object5 from sectors where (sectors.object1 = ?);",
                       (form.object1.data,))
            dvmypoisk = db.fetchall()
            device.rr = form.object1.data   #для фильтрации
            if dvmypoisk == []:
                flash(device.rr)
                return render_template('req.html', title='devices', form=form, dv=dv1, dvmy=dvmy,dvmypoisk=dvmypoisk,)
    if form.ppo.data == True:
        device.rr=None
        return redirect('/req')
    if form.addb.data == True:
        if form.object1.data == '':
            flash('Введите все поля')
            return redirect('/req')
        if form.object2.data == '':
            flash('Введите все поля')
            return redirect('/req')
        if form.object3.data == '':
            flash('Введите все поля')
            return redirect('/req')
        if form.object4.data == '':
            flash('Введите все поля')
            return redirect('/req')
        if form.object1.data != '':
            if form.object2.data != '':
                if form.object3.data != '':
                    if form.object4.data != '':
                                    conn.execute('insert into sectors (object1,object2,object3,object4,object5) values (?,?,?,?,?);',
                                                 (form.object1.data, form.object2.data, form.object3.data, form.object4.data, form.object5.data))
                                    conn.commit()
                                    flash('device_db_dob!')
                                    return render_template('req.html', title='requests', form=form, dv=dv1, dvmy=dvmy,
                                                           dvmypoisk=dvmypoisk)
    dov1 = form.gr_del_num.data
    dov2 = form.gr_del_num1.data
    if request.method == 'POST':
        if request.form['del'] == 'del':
            flash(dov2)
            conn.execute('delete from sectors where id_noms=? or id_noms=?',
                         (form.gr_del_num.data, form.gr_del_num1.data,) )
            conn.commit()
            flash('delete_ud!')
            return render_template('req.html', title='requests', form=form, dv=dv1, dvmy=dvmy,
                                   dvmypoisk=dvmypoisk)
    dv = dv1
    form.object1.data = device.rr # Для указания фильтрации в строке
    if device.rr!=None:
        db.execute(
            'select sectors.id_noms,sectors.object1, sectors.object2, sectors.object3, sectors.object4,sectors.object5 from sectors where (sectors.object1 = ?);',
            (device.rr,))
        dv1=db.fetchall()
        return render_template('req.html', title='requests', form=form, dv=dv1, dvmy=dvmy,
                               dvmypoisk=dvmypoisk)
    return render_template('req.html', title='requests', form=form, dv=dv, dvmy=dvmy, dvmypoisk=dvmypoisk)


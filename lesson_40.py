# ORM
# SQLAlchemy ORM

import os

from sqlalchemy import and_, or_, not_, desc

from models.database import DATABASE_NAME, Session
import create_database as db_creator

from models.lesson import Lesson, association_table
from models.student import Student
from models.group import Group

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
    print(session.query(Lesson).all())
    print("*" * 60)

    for it in session.query(Lesson):
        print(it)
    print("*" * 60)

    for it in session.query(Lesson):
        print(it.lesson_title)
    print("*" * 60)

    for it in session.query(Lesson).filter(Lesson.id >= 3):
        print(it.lesson_title)
    print("*" * 60)

    # Также можно использовать операторы COUNT и FIRST подобные. Пересмотреть этот момент перед перерывом.

    for it in session.query(Lesson).filter(Lesson.id >= 3, Lesson.lesson_title.like('Ф%')):
        print(it.lesson_title)
    print("*" * 60)

    for it in session.query(Lesson).filter(and_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
        print(it.lesson_title)
    print("*" * 60)

    for it in session.query(Lesson).filter(or_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
        print(it.lesson_title)
    print("*" * 60)

    for it in session.query(Lesson).filter(not_(Lesson.id >= 3), not_(Lesson.lesson_title.like('М%'))):
        print(it.lesson_title)
    print("*" * 60)

    for it in session.query(Lesson).filter(Lesson.lesson_title is None).all():
        print(it.lesson_title)
    print("*" * 60)

    for it in session.query(Lesson).filter(Lesson.lesson_title is not None).all():
        print(it.lesson_title)
    print("*" * 60)

    for it in session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Линейная алгебра'])).all():
        print(it.lesson_title)
    print("*" * 60)

    for it in session.query(Lesson).filter(Lesson.lesson_title.notin_(['Математика', 'Линейная алгебра'])).all():
        print(it.lesson_title)
    print("*" * 60)

    for it in session.query(Student).filter(Student.age.between(16, 17)).all():
        print(it)
    print("*" * 60)

    for it in session.query(Student).filter(not_(Student.age.between(17, 24))).all():
        print(it)
    print("*" * 60)

    for it in session.query(Student).filter(Student.age.like('1%')).all():
        print(it)
    print("*" * 60)

    for it in session.query(Student).filter(Student.age.like('1%')).limit(4):
        print(it)
    print("*" * 60)

    for it in session.query(Student).filter(Student.age.like('1%')).limit(4).offset(3):
        print(it)
    print("*" * 60)

    for it in session.query(Student).order_by(Student.surname):
        print(it)
    print("*" * 60)

    for it in session.query(Student).order_by(desc(Student.surname)):
        print(it)
    print("*" * 60)

    for it in session.query(Student).join(Group):
        print(it)
    print("*" * 60)

    for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-9'):
        print(it)
    print("*" * 60)

    #вторую половину только смотрел без записи отработать на практике!
import pytest
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from database import engine

# Создаем фабрику сессий
Session = sessionmaker(bind=engine)

@pytest.fixture(scope='function')
def session():
  """Создает новую сессию для каждого теста и откатывает изменения после."""
  session = Session()
  yield session
  # После теста откатываем все изменения, чтобы оставить базу в исходном состоянии
  session.rollback()
  session.close()

def test_add_student(session):
  # Добавляем нового студента с полями user_id, level, education_form, subject_id
  insert_stmt = text("""
    INSERT INTO student (user_id, level, education_form, subject_id)

    VALUES (:user_id, :level, :education_form, :subject_id)
    RETURNING user_id
  """)
  params = {
    'user_id': 12345,
    'level': 'Bachelor',
    'education_form': 'Full-time',
    'subject_id': 10
  }
  result = session.execute(insert_stmt, params)
  user_id = result.scalar()

  # Проверяем, что студент добавлен
  select_stmt = text("SELECT user_id, level, education_form, subject_id FROM student WHERE user_id=:user_id")
  student = session.execute(select_stmt, {'user_id': user_id}).fetchone()

  assert student is not None
  assert student['user_id'] == 12345
  assert student['level'] == 'Bachelor'
  assert student['education_form'] == 'Full-time'
  assert student['subject_id'] == 10

  # Удаляем созданного студента вручную
  delete_stmt = text("&DELETE FROM student WHERE user_id=:user_id")
  session.execute(delete_stmt, {'user_id': user_id})

def test_update_student(session):
  # Создаем временного студента для обновления
  insert_stmt = text("""
    INSERT INTO student (user_id, level, education_form, subject_id)
    VALUES (:user_id, :level, :education_form, :subject_id)
    RETURNING user_id

  """)
  params = {
    'user_id': 54321,
    'level': 'Master',
    'education_form': 'Part-time',
    'subject_id': 20
  }
  result = session.execute(insert_stmt, params)
  user_id = result.scalar()

  # Обновляем данные студента
  update_stmt = text("""
     UPDATE student SET level=:new_level, education_form=:new_education_form WHERE user_id=:user_id
  """)
  session.execute(update_stmt, {
    'new_level': 'PhD',
    'new_education_form': 'Online',
    'user_id': user_id
  })

  # Проверяем обновление
  select_stmt = text("SELECT level, education_form FROM student WHERE user_id=:user_id")
  student = session.execute(select_stmt, {'user_id': user_id}).fetchone()

  assert student['level'] == 'PhD'
  assert student['education_form'] == 'Online'

  # Удаляем временного студента
  delete_stmt = text("DELETE FROM student WHERE user_id=:user_id")
  session.execute(delete_stmt, {'user_id': user_id})

def test_delete_student(session):

  # Создаем временного студента для удаления
  insert_stmt = text("""
    INSERT INTO student (user_id, level, education_form, subject_id)
    VALUES (:user_id, :level, :education_form, :subject_id)
    RETURNING user_id
  """)
  params = {
    'user_id': 67890,
    'level': 'Bachelor',
    'subject_id': 15
  }
  result = session.execute(insert_stmt, params)
  user_id = result.scalar()

  # Удаляем студента
  delete_stmt = text("DELETE FROM student WHERE user_id=:user_id")
  session.execute(delete_stmt, {'user_id': user_id})

  # Проверяем удаление
  select_stmt = text("SELECT * FROM student WHERE user_id=:user_id")
  student = session.execute(select_stmt, {'user_id': user_id}).fetchone()

  assert student is None
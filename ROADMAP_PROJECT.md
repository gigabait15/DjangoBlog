# РЕАЛИЗАЦИЯ БЛОГА

## 1. структура проекта
### 1.1) Приложение блога:
#### 1) Поля модели:
- **Название(title)**
- **Контент(content)**
- **Изображение(image)** не приоритет, посмотреть как несколько изображений хранить в БД, для раскидки их по контексту
- **Автор(author)** по ключу FK
- **Дата и Время публикации(datetime publish)**
- **Количество просмотров(count view)**
- **Комментарии(comment)** пока не приоритет, в будущем реализовать
#### 2) Методы CRUD
#### У модели должен быть реализован следующий функционал:
- **Создание записи(create)**
- **Удаление записи(delete)**
- **Просмотр всех записей(list)** реализовать пагинацию, например по 5 статей, сделать динамическую подгрузку(если получиться)
- **Просмотр одной записи(detail)**
#### 3) Формы для работы
**Прописать формы для удобства работы с моделью**

### 1.2) Приложение Пользователя
#### 1) Поля модели:
- **Имя пользователя(username)**
- **Имя, Фамилия(fullname)** формировать из имени и фамилии одну строку
- **Email** 
- **Пароль(password)** 
#### 2) Методы CRUD
#### У модели должен быть реализован следующий функционал:
- **Создание пользователя(registration)**
- **Авторизация пользователя(auth)**
- **Удаление пользователя(delete)** не приоритет
- **Просмотр всех пользователей(list)** можно сделать одтельный лаунч, но опять не приоритет
- **Просмотр профиля(profile)**
#### 3) Формы для работы
**Прописать формы для удобства работы с моделью**
**Прописать clean методы для регистрации и авторизации**

### 1.3) Приложение Комментарии
#### 1) Поля модели:
- **Имя пользователя оставившего комментарий(comment_username)**
- **комментарии(comment)** 
- **Дата и Время когда оставили комментарий(datetime)**
#### 2) Методы CRUD
#### У модели должен быть реализован следующий функционал:
- **Создание комментария(create)**
- **Вывод всех комментариев для статьи(list)**
#### 3) Формы для работы
**Прописать формы для удобства работы с моделью**

### 2. Шаблоны
#### Нарисовать для всего шаблоны, использовать два(возможно больше) базовых шаблона.Один для всего проекта, второй для авторизации/регистрации

### 4. Доп. Функционал(utils)
#### 4.1) Прописать функцию создания БД
#### 4.2) Прописать функцию создания админа(superuser)
#### Возможно появиться необходимость еще в каком-то функционале, но пока я не знаю в каком

### 5. Nginx
#### Посмотреть как подключать к проекту

### 6. Redis
#### подключить к проекту. Для начала подключить к выводу статей
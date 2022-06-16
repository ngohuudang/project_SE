# Thông tin nhóm
| MSSV | Họ và Tên |
| :---: | :---: |
| 19120186 | Đỗ Lê Khánh Đăng | 
| 19120364 | Nguyễn Đắc Thắng | 
| 19120412 | Nguyễn Minh Tú |
| 19120462 |  Lục Minh Bửu |
| 19120467 | Ngô Hữu Đang |

# Giới thiệu project quản lí học sinh
- Chúng ta đang thực hiện chuyển đổi số, việc áp dụng công nghệ thông tin vào những công việc quản lý sẽ giúp ích rất nhiều.Đó là lí do nhóm xây dựng lên hệ thống quản lí học sinh
-  Hệ thống giúp ta quản lí  dữ liệu  an toàn, tổ chức, sắp xếp dữ liệu một cách khoa học để tránh phải làm những công việc lặp đi lặp lại.

# Môi trường thực thi

- Hệ điều hành Windows 10, Windows 11, Linux
- Framework: Django
- Database: MySQL

# Hướng dẫn chạy project 

**1. Tạo một thư mục (folder) mà bạn muốn lưu project**

**2. Tạo một môi trường trên máy và kích hoạt môi trường**

**Cài đặt môi trường**
```
pip install virtualenv
```

**Tạo môi trường**

Trên Windows
```
python -m venv venv
```
Trên Linux
```
virtualenv .
```

**Kích hoạt môi trường**

Trên Windows
```
source venv/scripts/activate
```

Trên Linux
```
source bin/activate
```

**3. Clone project**
```
git clone https://github.com/ngohuudang2001/project_SE.git
```

Chuyển đến thư mục chứa project
```
cd project_SE
```

**4. Cài đặt các thư viện từ 'requirements.txt'**
```python
pip3 install -r requirements.txt
```

**5. Database migration**
```python
python manage.py migrate
```

**6. Tạo tài khoản Admin(Super User)**
```python
python manage.py createsuperuser
``` 

**7. Chạy chương trình**
```python
python manage.py runserver
```

**8. Đăng nhập và sử dụng**

# Hướng dẫn deploy project lên Heroku
**1. Clone repo về máy cá nhân**
```
git clone <đường dẫn HTTPS của repo>
```
Sau đó cd vào repo vừa clone về

**2. Viết file requirements.txt**

Tạo file requirements.txt ở thư mục gốc của repo. Nội dung là tên các thư viện mà project cần sử dụng, và phiên bản của chúng nếu cần.

**3. Tạo file Procfile**

Tạo file Procfile ở thư mục gốc của repo để chỉ định cho heroku cách chạy project

**4. Chỉnh sửa settings.py**

- Thêm địa chỉ của heroku app, và localhost 127.0.0.1 vào ALLOWED_HOST
- Thêm đoạn code bên dưới vào cuối file:
```
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}
```

**5. Update schema**

```
python manage.py migrate
```

**6. Tạo heroku app**
```python
heroku create <tên app>
```

**7. Kết nối heroku app với repo hiện tại**
```python
heroku git:remote -a <tên app>
```
**8. Commit các thay đổi lên git**
```
git add .
git commit -m "<messages>"
```
**9. Push git repo lên heroku**
```
git push heroku <tên branch muốn push>
```

# Link demo trên Youtube 

# Các chức năng đã hoàn thành

# Các chức năng cần làm thêm

# Mobius-Project
Cách chạy trang web Mobius khi chưa cài đặt môi trường:
- Máy cần cài đặt Python và pip, tại folder Mobius-project mở cmd gõ lệnh pip install -r requirements.txt để cài đặt các gói cần thiết
- Cài đặt PgAdmin (PostgreSQL) bao gồm các thông tin cơ bản như: user, password, host, port
- Tạo một database tên Moibus
- Tạo file .env trong folder, copy nội dung trong file .env.dist và sửa các thông tin như lúc cài đặt PgAdmin
- Tại folder mở cmd gõ lệnh python manage.py makemigrations và python manage.py migrate để xác nhận các thay đổi
- Tạo super user trong Django bằng lệnh python manage.py createsuperuser
- Cuối cùng chạy web bằng lệnh python manage.py runserver


Cách chạy trang web Mobius trên máy ảo vlab Windows Server (môi trường đã cài đặt sẵn):
- Vào C:/Mobius-project
- Mở cmd và gõ lệnh python manage.py runserver 0.0.0.0:80 để chạy server
- Truy cập localhost:8000 để vào web ở local hoặc https://99e7f28ec9494edcbb53597e0d6d1763-1cd60300-vm-80.vlab2.uit.edu.vn để truy cập từ Internet

Các tính năng của web:
- Đăng kí
- Đăng nhập
- Đăng xuất
- Xem và thêm điện thoại vào giỏ hàng
- Xem chi tiết điện thoại
- Xem các bản tin công nghệ
- Tìm kiếm thông tin (điện thoại, phụ kiện,...)
- Chỉnh sửa thông tin cá nhân
- Thanh toán PayPal
- Còn tiếp 

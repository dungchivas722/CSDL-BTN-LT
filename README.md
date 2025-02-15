#  Hệ thống quản lý trường học ‍🎓

Hệ thống quản lý sinh viên hiện đại với các tính năng như: bảng điều khiển tương tác, quản lý điểm danh, cung cấp phản hồi, Tạo kết quả, đơn xin nghỉ phép

Website hiện tại đã đóng... hãy chạy local

## Phát triển 👨‍💻

Ghi chú : yêu cầu python trên 3.8

Công nghệ sử dụng: MySQL, Django, HTML, CSS, JavaScript

### Cách 1 : Dành cho người dùng phổ thông không cần cài đặt môi trường
 
Đường dẫn file tải xuống : [duncloud.online](https://duncloud.online/s/wgPRb2nRkKgkGoM)!

Giả nén file và chạy file `run_server.bat` để khởi chạy ứng dụng máy chủ

### Cách 2: Dành cho nhà phát triển cài đặt và phát triển

Cài Đặt Môi Trường 🚀

`$ git clone https://github.com/dungchivas722/CSDL-BTN-LT`

`$ cd CSDL-BTN-LT`

`$ python -m venv venv`

`$ source venv/Scripts/activate`

Cài đặt ưu tiên 🛠

`$ pip install -r requirements.txt`

Cuối cùng chay lệnh sau để khởi chạy ứng dụng

`$ python manage.py runserver`


## Cơ sở dữ liệu 📊

    'USER': "dun",
    'PASSWORD': "vqdung722001",
    'HOST': 'dunvps.online',
    'PORT': '7272'

- Cơ sở dữ liệu được sử dụng là MySQL và nó có thể remote trên máy chủ của nhóm


Tài khoản mặc định để đăng nhập vào hệ thống
---

**Vai trò quản trị**

    Email: admin@admin.com

    Password: admin

**Vai trò giảng viên**

    Email: staff@staff.com

    Password: staff

**Vai trò sinh viên**

    Email: student@student.com

    Password: student


---

### Quan hệ cơ sở dữ liệu 📚

![CSDL](https://raw.githubusercontent.com/dungchivas722/CSDL-BTN-LT/main/picture/bang.png)

## Hành Trình Dự Án 📝
- **Đăng nhập:**
  - Quản trị viên/Giảng viên/Sinh viên có thể đăng nhập hệ thống.

- **Quản lý khóa học:**
  - Thêm và chỉnh sửa khóa học.

- **Quản lý Giảng viên:**
  - Thêm và chỉnh sửa thông tin Giảng viên.
  - Tải lên ảnh của Giảng viên.

- **Quản lý sinh viên:**
  - Thêm và chỉnh sửa thông tin sinh viên.
  - Tải lên ảnh của sinh viên.

- **Quản lý môn học:**
  - Thêm và chỉnh sửa môn học.

- **Giao diện và Điều hướng:**
  - Trạng thái hoạt động của thanh bên.
  - Đặt tên URL động.
  - Truyền tiêu đề trang từ View - cải tiến.
  - Chuyển đổi tất cả liên kết sang dạng động.

- **Form và Mô hình:**
  - Form mô hình để thêm sinh viên.
  - Form mô hình dùng cho tất cả đối tượng.

- **Quyền hạn và Middleware:**
  - Quyền truy cập sử dụng `MiddleWareMixin`.

- **Điểm danh:**
  - Giảng viên thực hiện điểm danh và cập nhật điểm danh.
  - Sinh viên có thể kiểm tra điểm danh.
  - Quản trị viên xem điểm danh.

- **Quản lý nghỉ phép:**
  - Sinh viên có thể xin nghỉ phép.
  - Trả lời đơn xin nghỉ phép.

- **Phản hồi:**
  - Trả lời phản hồi từ sinh viên và Giảng viên.

- **Bảo mật:**
  - Đặt lại mật khẩu qua email.
  - Thay đổi mật khẩu cho quản trị viên, Giảng viên và sinh viên bằng `set_password()`.

- **Quản lý hồ sơ:**
  - Chỉnh sửa hồ sơ cho quản trị viên, Giảng viên và sinh viên.

- **Bảng điều khiển:**
  - Cố định bảng điều khiển cho sinh viên, Giảng viên và quản trị viên.

- **Thông báo:**
  - Tích hợp thông báo đẩy Firebase Web.

- **Quản lý kết quả:**
  - Giảng viên thêm kết quả sinh viên.
  - Giảng viên chỉnh sửa kết quả sử dụng CBV (Class Based Views).
  - Sinh viên xem kết quả.

- **Kiểm tra email:**
  - Kiểm tra tính khả dụng của email.

- **Tái cấu trúc mã:**
  - Tái cấu trúc mã để cải thiện hiệu suất và khả năng bảo trì (rất quan trọng).
---

### Tính năng 📌

### A. Quản Trị Viên Có Thể:
- Xem biểu đồ tổng quan về: 
  - Hiệu suất học tập của học sinh
  - Hiệu suất làm việc của nhân viên
  - Khóa học, môn học, nghỉ phép, v.v.
- Quản lý nhân viên (Thêm, Cập nhật và Xóa)
- Quản lý học sinh (Thêm, Cập nhật và Xóa)
- Quản lý khóa học (Thêm, Cập nhật và Xóa)
- Quản lý môn học (Thêm, Cập nhật và Xóa)
- Quản lý kỳ học (Thêm, Cập nhật và Xóa)
- Xem điểm danh học sinh
- Xem và trả lời phản hồi từ học sinh/nhân viên
- Duyệt (Chấp thuận/Từ chối) đơn xin nghỉ phép của học sinh/nhân viên

### B. Giảng Viên Có Thể:
- Xem biểu đồ tổng quan liên quan đến:
  - Học sinh của mình
  - Môn học của mình
  - Tình trạng nghỉ phép, v.v.
- Điểm danh và cập nhật điểm danh học sinh
- Thêm/Cập nhật kết quả học tập
- Nộp đơn xin nghỉ phép
- Gửi phản hồi đến Trưởng bộ môn (HOD)

### C. Học Sinh Có Thể:
- Xem biểu đồ tổng quan liên quan đến:
  - Điểm danh của mình
  - Môn học
  - Tình trạng nghỉ phép, v.v.
- Xem thông tin điểm danh
- Xem kết quả học tập
- Nộp đơn xin nghỉ phép
- Gửi phản hồi đến Trưởng bộ môn (HOD)

### Một số hình ảnh mẫu 📸

![1](https://raw.githubusercontent.com/dungchivas722/CSDL-BTN-LT/main/picture/1.png)
![2](https://raw.githubusercontent.com/dungchivas722/CSDL-BTN-LT/main/picture/2.png)
![3](https://raw.githubusercontent.com/dungchivas722/CSDL-BTN-LT/main/picture/3.png)
![4](https://raw.githubusercontent.com/dungchivas722/CSDL-BTN-LT/main/picture/4.png)

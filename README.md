 Mô tả giao diện web: Băm dữ liệu bằng SHA-256 và SHA-512
 
Chức năng:
Băm dữ liệu và kiểm tra thay đổi bằng thuật toán SHA

Mô tả chức năng:
Giao diện web cho phép người dùng nhập 2 đoạn văn bản (dữ liệu gốc và dữ liệu đã sửa), sau đó tiến hành băm (hash) dữ liệu bằng 2 thuật toán:

SHA-256

SHA-512

Kết quả hiển thị ra 4 mã băm tương ứng, giúp người dùng dễ dàng so sánh và kiểm tra tính toàn vẹn hoặc sự khác biệt dữ liệu.

Mục đích sử dụng:
Trình diễn tính chất "one-way" và nhạy cảm đầu vào của hàm băm

So sánh sự khác biệt khi chỉ sửa một chút dữ liệu

Ứng dụng cho học tập, bảo mật và kiểm tra tính toàn vẹn thông tin

Các thành phần chính trên giao diện:
    
Thành phần
Mô tả
 Dữ liệu gốc	
 
 Ô nhập văn bản ban đầu
 
 Dữ liệu đã sửa	Ô nhập văn bản đã thay đổi
 
 Nút “Băm”	Gửi dữ liệu lên server để xử lý
 
 Kết quả	Hiển thị mã SHA-256 & SHA-512 cho từng văn bản

Đặc điểm giao diện:
Giao diện đơn giản, gọn gàng, dễ thao tác

Màu nền nhẹ, khung mã băm nổi bật

Hộp kết quả dùng màu nhấn xanh lá (an toàn)

Tự động xuống dòng khi mã quá dài


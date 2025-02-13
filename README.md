# Phân Tích Dữ Liệu Phim TMDb

## Giới Thiệu

Dự án này thực hiện phân tích dữ liệu từ tập dữ liệu TMDb (The Movie Database), cung cấp thông tin về các bộ phim như ngày phát hành, doanh thu, điểm đánh giá, đạo diễn, diễn viên và thể loại.

## Mục Tiêu

- Xử lý dữ liệu thô và chuẩn hóa định dạng ngày tháng.
- Phân tích và lọc ra các bộ phim dựa trên các tiêu chí quan trọng.
- Xác định bộ phim có doanh thu cao nhất và thấp nhất.
- Tính toán tổng doanh thu của tất cả các bộ phim.
- Xác định đạo diễn có nhiều phim nhất và diễn viên tham gia nhiều phim nhất.
- Thống kê số lượng phim theo từng thể loại.

## Các Bước Xử Lý

### 1. Tiền Xử Lý Dữ Liệu

- Đọc dữ liệu từ file `tmdb-movies.csv`.
- Sửa lỗi định dạng ngày tháng bằng cách điều chỉnh năm (vì pandas tự động thêm "20**" vào năm khi chuyển đổi).
- Chuyển đổi một số cột quan trọng sang kiểu dữ liệu chuỗi (`str`).

### 2. Phân Tích Dữ Liệu

- **Sắp xếp các bộ phim theo ngày phát hành giảm dần** và lưu vào `sorted_by_date.csv`.
- **Lọc ra các bộ phim có điểm đánh giá trung bình trên 7.5** và lưu vào `filtered_by_vote_avg.csv`.
- **Xác định phim có doanh thu cao nhất và thấp nhất**.
- **Tính tổng doanh thu của tất cả các bộ phim**.
- **Lọc ra top 10 bộ phim có doanh thu cao nhất**.
- **Tìm đạo diễn có nhiều bộ phim nhất**.
- **Tìm diễn viên có số lần xuất hiện nhiều nhất**.
- **Thống kê số lượng phim theo thể loại**.

## Công Nghệ Sử Dụng

- **Python**: Ngôn ngữ chính để xử lý dữ liệu.
- **Pandas**: Thư viện hỗ trợ thao tác với dữ liệu dạng bảng.
- **Logging**: Ghi lại quá trình chạy của chương trình để kiểm tra và debug.

## Kết Quả Chính

- **Bộ phim có doanh thu cao nhất**: `{Tên phim}` với doanh thu `{Số tiền}`.
- **Bộ phim có doanh thu thấp nhất**: `{Tên phim}` với doanh thu `{Số tiền}`.
- **Tổng doanh thu của tất cả các bộ phim**: `{Số tiền}`.
- **Đạo diễn có nhiều bộ phim nhất**: `{Tên đạo diễn}`.
- **Diễn viên đóng nhiều phim nhất**: `{Tên diễn viên}`.
- **Thể loại phổ biến nhất**: `{Tên thể loại}` với `{Số lượng}` bộ phim.

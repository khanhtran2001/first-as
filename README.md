# ASSIGNMENT 1: ANNOTATION DATA
first-assignment-MapleYuna created by GitHub Classroom

## 1. Thu thập dữ liệu
- Dữ liệu lưu trong thư mục **_face_data_** trong đó có 50 ảnh raw

## 2.1 Annotate dữ liệu (Manual)
- Sử dụng tool **Labelme** để annotate đối tượng là khuôn mặt, dữ liệu đầu ra là các file **.json** được lưu trong thư mục **_face_data_json_**

> * **Input:** 50 ảnh raw
> * **Output:** 50 file **.json**

## 2.2 Annotate dữ liệu (Haar Cascode)
- Sử dụng Haar Cascade cắt trực tiếp đc mặt ra từ ảnh raw
- Chương trình cắt khuôn mặt từ ảnh raw được lưu trong file `Annotate_haar_cascode.py`
- Sau khi cắt xong, ảnh được lưu trong thư mục **_annotated_face_data_haar_cascode_**

> * **Input:** 50 ảnh raw
> * **Output:** 50 ảnh mặt đã được cắt ra

## 3. Viết chương trình cắt ra vùng khuôn mặt đã annotate (Manual)
- Chương trình được viết ở file `Annotate_manual.py`

> * **Input:** 50 ảnh raw và 50 file **.json**
> * **Output:** 50 ảnh mặt đã được cắt ra

## 4. Sử dụng tSNE visualize các khuôn mặt vừa nhận được
(Chưa hoàn thành)

### Hạn chế
- Chương trình mới chỉ nhận diện được các ảnh có 1 khuôn mặt

Track 3
ระบบจัดการแผนการเรียนภาควิชาวิศวกรรมคอมพิวเตอร์ โดยใช้โครงสร้างข้อมูลแบบ Maps (Hash Tables)

คุณสมบัติ (Features)
- `show_semester`: แสดงรายชื่อวิชาแยกตามภาคเรียน
- `total_credits`: คำนวณหน่วยกิตรวมรายภาคเรียนแบบ Real-time
- `plan_summary`: สรุปแผนการเรียนรายปี (Year 1 - Year 4)

โครงสร้างข้อมูลที่ใช้ (Data Structures)
- Hash Map (Dictionary): ใช้ `Semester` เป็น Key เพื่อการเข้าถึงข้อมูลที่รวดเร็ว (O(1))
- Data Aggregation(การรวมกลุ่ม): อัลกอริทึมการคำนวณหน่วยกิตโดยการประมวลผลข้อมูลจาก Map

วิธีการใช้งานบนcolab (Usage)
1. สร้างไฟล์ของCOLABขึ้นมา
2. อัพโหลดไฟล์ CprE_Subject.csv
3. รันcodeจากที่นำมาจาก Main.py

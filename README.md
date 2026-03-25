Track 3
ระบบจัดการแผนการเรียนภาควิชาวิศวกรรมคอมพิวเตอร์ โดยใช้โครงสร้างข้อมูลแบบ Maps (Hash Tables)

คุณสมบัติ (Features)
- `show_semester`: แสดงรายชื่อวิชาแยกตามภาคเรียน
- `total_credits`: คำนวณหน่วยกิตรวมรายภาคเรียนแบบ Real-time
- `plan_summary`: สรุปแผนการเรียนรายปี (Year 1 - Year 4)

โครงสร้างข้อมูลที่ใช้ (Data Structures)
- Hash Map (Dictionary): ใช้ `Semester` เป็น Key เพื่อการเข้าถึงข้อมูลที่รวดเร็ว (O(1))
- Data Aggregation: อัลกอริทึมการคำนวณหน่วยกิตโดยการประมวลผลข้อมูลจาก Map

วิธีการใช้งาน (Usage)
1. ติดตั้ง Library: `pip install pandas tabulate`
2. รันไฟล์: `python main.py`

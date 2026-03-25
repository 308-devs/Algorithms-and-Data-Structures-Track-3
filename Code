import pandas as pd

class CoursePlanner:
    def __init__(self, file_path):
        try:
            # อ่านไฟล์และลบช่องว่างที่ชื่อคอลัมน์
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.strip()

            # --- Data Structure: Maps/Hash Table (ใช้ชื่อ semester ตามที่ต้องการ) ---
            self.semester = {}
            for _, row in df.iterrows():
                sem_key = int(float(row['Semester']))
                if sem_key not in self.semester:
                    self.semester[sem_key] = []
                self.semester[sem_key].append(row.to_dict())

            print("✅ โหลดข้อมูลรายวิชาเรียบร้อยแล้ว")
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาด: {e}")
            self.semester = {}

    def show_semester(self, num):
        """Lists all courses in that specific semester"""
        courses = self.semester.get(num)
        if courses:
            print(f"\n>> show_semester {num}")
            for c in courses:
                code = c.get('CourseCode', 'N/A')
                name = c.get('Name', 'N/A')
                # ดึงเลขหน่วยกิตตัวแรก เช่น 3(3-0) -> 3
                credit = str(c.get('Credit', '0'))[0]
                print(f"- {code}: {name} ({credit})")
        else:
            print(f"⚠️ ไม่พบข้อมูลในเทอม {num}")

    def total_credits(self, num):
        """Sum credits for that semester"""
        courses = self.semester.get(num)
        if courses:
            total = sum(int(str(c.get('Credit', '0'))[0]) for c in courses)
            print(f"\n>> total_credits {num}")
            print(f"Found {len(courses)} courses. Total: {total} Credits.")
        else:
            print(f"⚠️ ไม่พบข้อมูลในเทอม {num}")

    def plan_summary(self):
        """Shows Year 1 (Sem 1+2), Year 2 (Sem 3+4), etc."""
        if not self.semester: return

        print("\n>> plan_summary")
        # หาเทอมสูงสุดที่มีเพื่อคำนวณจำนวนปี
        max_sem = max(self.semester.keys())
        max_year = (max_sem + 1) // 2

        for year in range(1, max_year + 1):
            s1, s2 = (year * 2) - 1, (year * 2)
            # ดึงข้อมูลจาก Map (ถ้าไม่มีให้เป็น List ว่าง)
            c1 = self.semester.get(s1, [])
            c2 = self.semester.get(s2, [])

            t1 = sum(int(str(c.get('Credit', '0'))[0]) for c in c1)
            t2 = sum(int(str(c.get('Credit', '0'))[0]) for c in c2)

            print(f"Year {year}: {t1 + t2} Credits")

    def run_menu(self):
        while True:
            print("\n" + "="*45)
            print("  🎓 CPRe Course Planner (CLI Menu)")
            print("="*45)
            print("  1. show_semester")
            print("  2. total_credits")
            print("  3. plan_summary")
            print("  4. exit")
            print("-" * 45)

            choice = input("เลือกเมนู (1-4): ").strip()

            if choice == '1':
                try:
                    n = int(input("กรอกเลขเทอม: "))
                    self.show_semester(n)
                except ValueError: print("❌ กรุณากรอกเป็นตัวเลข")
            elif choice == '2':
                try:
                    n = int(input("กรอกเลขเทอม: "))
                    self.total_credits(n)
                except ValueError: print("❌ กรุณากรอกเป็นตัวเลข")
            elif choice == '3':
                self.plan_summary()
            elif choice == '4':
                print("👋 ปิดโปรแกรม...")
                break
            else:
                print("❌ คำสั่งไม่ถูกต้อง")

# --- เริ่มรัน ---
planner = CoursePlanner('CprE_Subject.csv')
planner.run_menu()

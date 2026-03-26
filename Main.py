import pandas as pd

class CoursePlanner:
    def __init__(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df.columns = df.columns.str.strip()
            self.semester = {}
            for _, row in df.iterrows():
                sem_key = int(float(row['Semester']))
                if sem_key not in self.semester:
                    self.semester[sem_key] = []
                self.semester[sem_key].append(row.to_dict())
            print("✅ โหลดข้อมูลและจัดโครงสร้างแบบ Map เรียบร้อยแล้ว")
        except Exception as e:
            print(f"❌ Error: {e}")
            self.semester = {}

    def recursive_sum(self, course_list):
        if not course_list:
            return 0
        
        current_credit = int(str(course_list[0].get('Credit', '0'))[0])
        return current_credit + self.recursive_sum(course_list[1:])

    def show_semester(self, num):
        courses = self.semester.get(num)
        if courses:
            print(f"\n>> show_semester {num}")
            for c in courses:
                print(f"- {c['CourseCode']}: {c['Name']} ({str(c['Credit'])[0]})")
        else:
            print(f"⚠️ ไม่พบข้อมูลเทอม {num}")

    def total_credits(self, num):
        courses = self.semester.get(num, [])
        if courses:
            total = self.recursive_sum(courses)
            print(f"\n>> total_credits {num}")
            print(f"Total: {total} Credits.")
        else:
            print(f"⚠️ ไม่พบข้อมูล")

    def plan_summary(self):
        if not self.semester: return
        print("\n>> plan_summary")
        max_sem = max(self.semester.keys())
        max_year = (max_sem + 1) // 2
        
        for year in range(1, max_year + 1):
            s1, s2 = (year * 2) - 1, (year * 2)
            combined_courses = self.semester.get(s1, []) + self.semester.get(s2, [])
            total = self.recursive_sum(combined_courses)
            print(f"Year {year}: {total} Credits")

    def run_menu(self):
        while True:
            print("\n" + "="*45)
            print("  🎓 CPRe Course Planner ")
            print("="*45)
            print("  1. show_semester\n  2. total_credits\n  3. plan_summary\n  4. exit")
            choice = input("เลือกเมนู: ").strip()
            if choice == '1':
                try: self.show_semester(int(input("กรอกเลขเทอม: ")))
                except: print("❌ กรุณากรอกตัวเลข")
            elif choice == '2':
                try: self.total_credits(int(input("กรอกเลขเทอม: ")))
                except: print("❌ กรุณากรอกตัวเลข")
            elif choice == '3': self.plan_summary()
            elif choice == '4': break

planner = CoursePlanner('CprE_Subject.csv')
planner.run_menu()

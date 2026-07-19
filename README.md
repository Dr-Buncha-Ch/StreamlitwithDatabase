อ้างอิง https://github.com/Dr-Buncha-Ch/Streamlit.Begin.git 
- เพิ่มฟังก์ชันฐานข้อมูล 5 ตัว: get_connection, init_db, add_task_db, get_all_tasks_db, delete_task_db
- จุดสำคัญที่ควรเน้น: การลบข้อมูลเปลี่ยนจากใช้ index ในลิสต์ มาเป็น id จริงในฐานข้อมูล
- ปรับ CSS : ใส่ฟอนต์ Poppins, เพิ่ม gradient ทับพื้นหลัง sidebar ให้ตัวหนังสือขาวอ่านง่าย, ปุ่มไล่สี+เงา+เอฟเฟกต์ hover, กรอบ input ตอน focus, เงาที่ตาราง (รายละเอียดทั้งหมดพร้อมตาราง before/after อยู่ในไฟล์ worksheet)

🐍 ขั้นตอนการสร้าง Virtual Environment (venv)
A. เปิดโฟลเดอร์โปรเจกต์
B. เปิด Terminal ภายในโฟลเดอร์
C. สร้าง Virtual Environment
	python -m venv .venv

D. เปิดใช้งาน Virtual Environment
	.venv\Scripts\Activate.ps1


E. ติดตั้ง Streamlit
	pip install streamlit
  ตรวจสอบ
	streamlit version


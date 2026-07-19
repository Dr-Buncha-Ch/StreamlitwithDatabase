import streamlit as st
import pandas as pd
import sqlite3
import streamlit.components.v1 as components

# =====================================================
# 🧩 แบบฝึกหัด : เติมฟังก์ชันฐานข้อมูล SQLite ให้ครบ
# =====================================================
# วิธีทำ:
#   1. อ่านเอกสารประกอบ "worksheet_database_exercise.md"
#   2. ในเอกสารจะมี "ชิ้นส่วนโค้ด" (Code Pieces) สลับลำดับกันอยู่
#   3. ให้นักเรียนเลือกชิ้นส่วนที่ถูกต้อง มาเรียงลำดับ แล้ววางแทนที่
#      คอมเมนต์ TODO ด้านล่างของแต่ละฟังก์ชัน
#   4. ห้ามแก้ชื่อฟังก์ชัน / พารามิเตอร์ที่ให้มาแล้ว
#
# หมายเหตุ: ส่วนอื่นของโปรแกรม (การแสดงผล, เมนู, CSS ฯลฯ) ทำงานได้แล้ว
#           งานของนักเรียนคือทำให้ฟังก์ชันฐานข้อมูล 5 ฟังก์ชันด้านล่างทำงานได้จริง
DB_NAME = "tasks.db"


def get_connection():
    """เปิดการเชื่อมต่อฐานข้อมูล (สร้างไฟล์ tasks.db อัตโนมัติถ้ายังไม่มี)"""
    # 🧩 TODO 1: เติม 1 บรรทัด
    # คำใบ้: ต้อง "return" ค่าการเชื่อมต่อฐานข้อมูล โดยใช้ sqlite3
    pass


def init_db():
    """สร้างตาราง tasks ถ้ายังไม่มี"""
    # 🧩 TODO 2: เติม 4 บรรทัด ตามลำดับนี้
    # 1) ขอการเชื่อมต่อฐานข้อมูล (เรียกใช้ get_connection)
    # 2) สร้างตัวแปร cursor จาก conn
    # 3) สั่ง cursor ให้สร้างตาราง tasks (ถ้ายังไม่มี) มีคอลัมน์ id, task, status
    # 4) บันทึกการเปลี่ยนแปลง (commit) และปิดการเชื่อมต่อ (close)
    pass


def add_task_db(task, status):
    """เพิ่มข้อมูลลงตาราง tasks"""
    # 🧩 TODO 3: เติม 4 บรรทัด
    # 1) เปิดการเชื่อมต่อ
    # 2) สร้าง cursor
    # 3) สั่ง INSERT ข้อมูล task และ status ลงตาราง
    # 4) commit และ close
    pass


def get_all_tasks_db():
    """ดึงข้อมูลทั้งหมดจากตาราง tasks กลับมาเป็น DataFrame"""
    # 🧩 TODO 4: เติม 3 บรรทัด
    # 1) เปิดการเชื่อมต่อ
    # 2) ใช้ pd.read_sql_query อ่านข้อมูลทั้งหมดจากตาราง tasks
    # 3) close การเชื่อมต่อ แล้ว return ข้อมูลที่ได้
    pass


def delete_task_db(task_id):
    """ลบข้อมูลตาม id จริงในฐานข้อมูล"""
    # 🧩 TODO 5: เติม 4 บรรทัด
    # 1) เปิดการเชื่อมต่อ
    # 2) สร้าง cursor
    # 3) สั่ง DELETE แถวที่มี id ตรงกับ task_id
    # 4) commit และ close
    pass


# -----------------------------
# CSS Design
# -----------------------------
def load_css():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    section[data-testid="stSidebar"] {
        background-image:
            linear-gradient(rgba(10, 20, 40, 0.65), rgba(10, 20, 40, 0.65)),
            url("https://images.unsplash.com/photo-1516321318423-f06f85e504b3");
        background-size: cover;
        background-position: center;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    h1 {
        color: #1f77b4;
        text-align: center;
        letter-spacing: 0.5px;
    }

    h2 {
        color: #2e8b57;
        border-bottom: 2px solid #eaf4ff;
        padding-bottom: 6px;
    }

    .stButton button {
        background: linear-gradient(135deg, #1f77b4, #0b5394);
        color: white;
        border: none;
        border-radius: 10px;
        height: 42px;
        font-size: 16px;
        font-weight: 600;
        box-shadow: 0 2px 6px rgba(31, 119, 180, 0.35);
        transition: all 0.2s ease-in-out;
    }

    .stButton button:hover {
        background: linear-gradient(135deg, #0b5394, #08356b);
        color: #ffe600;
        box-shadow: 0 4px 10px rgba(11, 83, 148, 0.45);
        transform: translateY(-1px);
    }

    .stTextInput input {
        border-radius: 10px;
        border: 1px solid #cfd8dc;
    }

    .stTextInput input:focus {
        border: 1px solid #1f77b4;
        box-shadow: 0 0 0 2px rgba(31, 119, 180, 0.15);
    }

    section[data-testid="stSidebar"] {
        background-color: #eaf4ff;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        overflow: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True)


# -----------------------------
# Home Page
# -----------------------------
def home_page():
    st.header("🏠 Welcome")
    st.write("""
    โปรแกรมตัวอย่างสำหรับฝึก

    - Function
    - CRUD
    - Database (SQLite)
    - Session State
    - Streamlit
    """)


# -----------------------------
# Add Task
# -----------------------------
def add_task():

    st.header("➕ Add Task")

    st.info("JavaScript Example : แสดงจำนวนตัวอักษรที่พิมพ์")

    components.html("""

    <div style="
        border:1px solid #dddddd;
        padding:15px;
        border-radius:10px;
        background:#f8f9fa;
    ">

    <label><b>Task Preview (JavaScript)</b></label>

    <input
        id="taskInput"
        type="text"
        placeholder="Type task here..."
        style="
            width:95%;
            padding:8px;
            margin-top:8px;
        "
        onkeyup="countText()"
    >

    <p id="count">
        Characters : 0
    </p>

    <script>

    function countText(){

        let txt =
            document.getElementById("taskInput").value;

        document.getElementById("count").innerHTML =
            "Characters : " + txt.length;

    }

    </script>

    </div>

    """, height=170)

    st.divider()

    task = st.text_input("Task Name")

    status = st.selectbox(
        "Status",
        ["Pending", "Done"]
    )

    if st.button("Save"):

        if task.strip() == "":
            st.warning("Please enter task")
            return

        add_task_db(task, status)

        st.success("Add Success")


# -----------------------------
# Show Tasks
# -----------------------------
def show_tasks():
    st.header("📄 Task List")

    df = get_all_tasks_db()

    if df is None or df.empty:
        st.info("No Data")
        return

    df = df.rename(columns={"id": "ID", "task": "Task", "status": "Status"})
    df = df.set_index("ID")

    st.dataframe(
        df,
        use_container_width=True
    )


# -----------------------------
# Delete Task
# -----------------------------
def delete_task():
    st.header("🗑 Delete Task")

    df = get_all_tasks_db()

    if df is None or df.empty:
        st.info("No Data")
        return

    options = [
        f"{row.id}. {row.task} ({row.status})"
        for row in df.itertuples()
    ]
    ids = df["id"].tolist()

    selected = st.selectbox(
        "Select Task",
        range(len(options)),
        format_func=lambda x: options[x]
    )

    if st.button("Delete"):

        delete_task_db(ids[selected])

        st.success("Delete Success")
        st.rerun()


# -----------------------------
# Footer
# -----------------------------
def footer():

    st.markdown("""
    <hr>

    <div style="
        text-align:center;
        color:gray;
        font-size:14px;
    ">

        Powered by 
        Team name :
        
        Student Development Team

    </div>

    """,
    unsafe_allow_html=True)


# -----------------------------
# Main Program
# -----------------------------
def main():

    st.set_page_config(
        page_title="Student Task Manager",
        page_icon="📋",
        layout="wide"
    )

    load_css()

    init_db()

    st.title("📋 Student Task Manager")

    st.sidebar.image(
        "https://static.vecteezy.com/system/resources/thumbnails/022/418/057/small_2x/project-task-management-and-effective-time-planning-tools-project-development-icon-3d-vector-illustration-png.png",
        width=250
    )

    st.sidebar.title(
        "Student Manager"
    )

    menu = st.sidebar.selectbox(
        "📋 Menu",
        [
            "🏠 Home",
            "➕ Add Task",
            "📄 Show Tasks",
            "🗑 Delete Task"
        ]
    )

    if menu == "🏠 Home":
        home_page()

    elif menu == "➕ Add Task":
        add_task()

    elif menu == "📄 Show Tasks":
        show_tasks()

    elif menu == "🗑 Delete Task":
        delete_task()


if __name__ == "__main__":
    main()

footer()

with st.expander("📦 Session State (สำหรับการเรียนรู้)"):
    st.write(st.session_state)

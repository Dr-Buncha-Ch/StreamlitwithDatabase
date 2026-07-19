import streamlit as st
import pandas as pd
import sqlite3
import streamlit.components.v1 as components

# =====================================================
# ⭐ ส่วนที่เพิ่มใหม่ : การเชื่อมต่อฐานข้อมูล SQLite
# =====================================================
# เดิม: โปรแกรมเก็บข้อมูลไว้ใน st.session_state.tasks (อยู่ใน RAM)
#       -> พอปิดโปรแกรม/รีเฟรชหน้าเว็บ ข้อมูลหายหมด
# ใหม่: เก็บข้อมูลลงไฟล์ tasks.db (ฐานข้อมูล SQLite)
#       -> ข้อมูลอยู่ถาวร ปิดโปรแกรมแล้วเปิดใหม่ก็ยังอยู่
DB_NAME = "tasks.db"


def get_connection():
    """เปิดการเชื่อมต่อฐานข้อมูล (สร้างไฟล์ tasks.db อัตโนมัติถ้ายังไม่มี)"""
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def init_db():
    """สร้างตาราง tasks ถ้ายังไม่มี (แทนที่ init_data เดิม)"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_task_db(task, status):
    """เพิ่มข้อมูลลงตาราง tasks (แทน .append เดิม)"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (task, status) VALUES (?, ?)",
        (task, status)
    )
    conn.commit()
    conn.close()


def get_all_tasks_db():
    """ดึงข้อมูลทั้งหมดจากตาราง tasks กลับมาเป็น DataFrame"""
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM tasks", conn)
    conn.close()
    return df


def delete_task_db(task_id):
    """ลบข้อมูลตาม id จริงในฐานข้อมูล (แทนการ .pop(index) เดิม)"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


# -----------------------------
# CSS Design (⭐ ปรับปรุงให้ดูมืออาชีพขึ้น)
# -----------------------------
def load_css():

    st.markdown("""
    <style>

    /* ⭐ เพิ่ม: ใช้ฟอนต์ที่ดูสะอาดตาและเป็นมืออาชีพขึ้น */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* Sidebar Background Image */
    section[data-testid="stSidebar"] {

        /* ⭐ ปรับ: เพิ่ม gradient สีเข้มทับรูปภาพ เพื่อให้ตัวหนังสือสีขาวอ่านง่ายขึ้น
           (ของเดิมใช้รูปอย่างเดียว ตัวหนังสือขาวจะจมไปกับรูปบางจุด) */
        background-image:
            linear-gradient(rgba(10, 20, 40, 0.65), rgba(10, 20, 40, 0.65)),
            url("https://images.unsplash.com/photo-1516321318423-f06f85e504b3");

        background-size: cover;
        background-position: center;
    }

    /* ทำให้ข้อความ Sidebar อ่านง่าย */
    section[data-testid="stSidebar"] * {
        color: white;
    }

    /* หัวข้อหลัก */
    h1 {
        color: #1f77b4;
        text-align: center;
        letter-spacing: 0.5px;      /* ⭐ เพิ่ม: ระยะห่างตัวอักษรให้ดูโปร่งสบายตา */
    }

    /* หัวข้อย่อย */
    h2 {
        color: #2e8b57;
        border-bottom: 2px solid #eaf4ff;  /* ⭐ เพิ่ม: เส้นใต้บาง ๆ แบ่งหัวข้อ */
        padding-bottom: 6px;
    }

    /* ปุ่ม */
    .stButton button {
        background: linear-gradient(135deg, #1f77b4, #0b5394); /* ⭐ ปรับ: ไล่สีแทนสีเรียบ */
        color: white;
        border: none;
        border-radius: 10px;
        height: 42px;
        font-size: 16px;
        font-weight: 600;
        box-shadow: 0 2px 6px rgba(31, 119, 180, 0.35); /* ⭐ เพิ่ม: เงาให้ดูมีมิติ */
        transition: all 0.2s ease-in-out;               /* ⭐ เพิ่ม: เอฟเฟกต์ลื่นไหล */
    }

    /* ตอนเอาเมาส์ชี้ปุ่ม */
    .stButton button:hover {
        background: linear-gradient(135deg, #0b5394, #08356b);
        color: #ffe600;
        box-shadow: 0 4px 10px rgba(11, 83, 148, 0.45);
        transform: translateY(-1px);   /* ⭐ เพิ่ม: ปุ่มยกตัวขึ้นเล็กน้อยตอน hover */
    }

    /* ช่องกรอกข้อมูล */
    .stTextInput input {
        border-radius: 10px;
        border: 1px solid #cfd8dc;
    }

    .stTextInput input:focus {
        border: 1px solid #1f77b4;                       /* ⭐ เพิ่ม: เน้นกรอบตอนคลิกกรอก */
        box-shadow: 0 0 0 2px rgba(31, 119, 180, 0.15);
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #eaf4ff;
    }

    /* ตาราง */
    div[data-testid="stDataFrame"] {
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);  /* ⭐ เพิ่ม: เงาให้ตารางดูลอยขึ้นมาเล็กน้อย */
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

    # -------------------------
    # JavaScript Example
    # -------------------------
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

    # -------------------------
    # Streamlit Form
    # -------------------------

    task = st.text_input("Task Name")

    status = st.selectbox(
        "Status",
        ["Pending", "Done"]
    )

    if st.button("Save"):

        if task.strip() == "":
            st.warning("Please enter task")
            return

        # ⭐ ปรับ: เดิมใช้ st.session_state.tasks.append({...})
        #          ตอนนี้เรียกฟังก์ชันฐานข้อมูลแทน
        add_task_db(task, status)

        st.success("Add Success")


# -----------------------------
# Show Tasks
# -----------------------------
def show_tasks():
    st.header("📄 Task List")

    # ⭐ ปรับ: เดิมอ่านจาก st.session_state.tasks
    #          ตอนนี้อ่านจากฐานข้อมูลด้วย get_all_tasks_db()
    df = get_all_tasks_db()

    if df.empty:
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

    # ⭐ ปรับ: ดึงข้อมูลจากฐานข้อมูลแทน list ใน session_state
    df = get_all_tasks_db()

    if df.empty:
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

        # ⭐ ปรับ: เดิมลบด้วย .pop(index) ในตัวแปรความจำ
        #          ตอนนี้ลบด้วย id จริงในฐานข้อมูล (สำคัญมาก! ไม่ใช่ index)
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

    # โหลด CSS
    load_css()

    # ⭐ ปรับ: เดิมเรียก init_data() (สร้าง list ว่างใน session_state)
    #          ตอนนี้เรียก init_db() (สร้างตารางในฐานข้อมูลถ้ายังไม่มี)
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


# -----------------------------
# Start Program
# -----------------------------
if __name__ == "__main__":
    main()

# แสดง Footer ทุกหน้า
footer()

# =====================================================
# DEBUG (ใช้สอน)
# =====================================================
# ⭐ หมายเหตุ: st.session_state.tasks จะไม่มีอีกต่อไปเพราะย้ายไปฐานข้อมูลแล้ว
#            ให้ลองเปิดไฟล์ tasks.db ด้วยโปรแกรม DB Browser for SQLite ดูได้
with st.expander("📦 Session State (สำหรับการเรียนรู้)"):
    st.write(st.session_state)

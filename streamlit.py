import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

API = "http://127.0.0.1:8000"

st.title("Employee System")

choice = st.sidebar.radio("Menu", ["Dashboard", "Manage Employees"])

if choice == "Dashboard":
    st.header("Dashboard")

    data = requests.get(f"{API}/employees").json()
    df = pd.DataFrame(data)

    st.subheader("Employee Table")
    st.dataframe(df)

    if not df.empty:
        st.subheader("average salary")
        st.write(df["salary"].mean())

        st.subheader("employees/department")
        st.bar_chart(df["department"].value_counts())

        st.subheader("salary distribution")
        fig, ax = plt.subplots()
        ax.hist(df["salary"])
        st.pyplot(fig)


else:
    st.header("Manage Employees")

    st.subheader("add employee")
    name = st.text_input("name")
    dept = st.text_input("department")
    salary = st.number_input("salary")
    hire = st.date_input("hire date")

    if st.button("ADD"):
        requests.post(f"{API}/employees", json={
            "name": name,
            "department": dept,
            "salary": salary,
            "hire_date": str(hire)
        })
        st.success("employee added")

    st.subheader("Update / Delete")
    data = requests.get(f"{API}/employees").json()

    if data:
        ids = [e["employee_id"] for e in data]
        selected = st.selectbox("Select ID", ids)
        emp = requests.get(f"{API}/employees/{selected}").json()

        name2 = st.text_input("Edit Name", emp["name"])
        dept2 = st.text_input("Edit Department", emp["department"])
        sal2 = st.number_input("Edit Salary", value=float(emp["salary"]))
        hire2 = st.date_input("Edit Hire Date")

        if st.button("Update"):
            requests.put(f"{API}/employees/{selected}", json={
                "name": name2,
                "department": dept2,
                "salary": sal2,
                "hire_date": str(hire2)
            })
            st.success("Updated!")

        if st.button("Delete"):
            requests.delete(f"{API}/employees/{selected}")
            st.error("Deleted!")
    else:
        st.write("No employees available.")

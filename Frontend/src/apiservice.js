import axios from 'axios'

export async function get_Current_Students() {
    const res = await axios({
        method: "get",
        url: `/api/StudentRecords/currentstudents`
      })
    return res.data.data
}

export async function get_Students(start=null, end=null) {
    let url = `/api/StudentRecords/students`

    if (start != null && end != null) {
        url += `?start=${start}&end=${end}`
    }

    let res = await axios({
        method: "get",
        url: url
    })

    return res.data.data
}

export async function delete_student(id) {
    const res = await axios.delete(`/api/StudentRecords/delete-student?id=${id}`)
    return res.data.ok
}

export async function get_Student(id) {
    const res = await axios.get(`/api/StudentRecords/student?id=${id}`)
    return res.data.data
}

export async function edit_student(student) {
    const res = await axios.put("/api/StudentRecords/edit-student", student)
    return res.data.data
}

export async function add_student(student) {
    const res = await axios.post("/api/StudentRecords/add-student", student)
    return res.data.data
}
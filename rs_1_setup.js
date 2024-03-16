try {
    if (rs.status().ok === 1) {
        console.log("Replica Set is already instantiated")
        exit
    }
} catch (e) {
    if (e.ok === 0) {
        rs.initiate(
            {
                _id: "mongo_rs1",
                members: [
                    {_id: 0, host: "mongo_rs1_n1"},
                    {_id: 1, host: "mongo_rs1_n2"}
                ]
            })
        console.log("Replica Set instantiated")
    } else {
        throw e
    }
}

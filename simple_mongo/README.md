```shell
show databases
```

```shell
use test_db
```

```shell
db.createCollection('users')
```

```shell
db.dropDatabase()
```

#### Создадим заново:

```shell
use test_db
```

```shell
db.createCollection('users')
```

```shell
show collections
```

```shell
db.users.insert({
  name: "Super user",
  age: 55
})
```

```shell
db.users.insertOne({
  name: "Another user",
  age: 45
})
```

```shell
db.users.find()
```

```shell
db.users.insertMany([
  { name: "Степан Богданович", age: 23 },
  { name: "Григорий Данилович", age: 21 },
  { name: "Иван Савельевич", age: 67 },
  { name: "Никанор Иванович", age: 190 },
  { name: "Михаил Александрович", age: 11 },
  { name: "Арчибальд Арчибальдович", age: 78 },
])
```

```shell
db.users.find({
  age: 67
})
```

```shell
db.users.find({
  age: 67, name: "Иван"
})
```


```shell
db.users.find({
  age: 67, name: "Иван Савельевич"
})
```

```shell
db.users.find({
  $or: [
    { age: 23 },
    { name: "Арчибальд Арчибальдович" }
  ]
})
```

```shell
db.users.find({
  age: {
    $lt: 30
  }
})
```

```shell
db.users.find({
  age: {
    $gte: 67
  }
})
```

```shell
db.users.find({
  age: {
    $ne: 67
  }
})
```

```shell
db.users.find({
  age: {
    $ne: 190
  }
})
```

```shell
db.users.find().sort( { age: 1 })
```

```shell
db.users.find().sort( { age: -1 })
```

```shell
db.users.find().limit(3)
```

```shell
db.users.findOne({ _id: ObjectId('65f98fb9cf79a5fac27e428f') })
```

```shell
db.users.updateOne(
  { name: "Степан Богданович" },{
    $set: {
      age: 61
    }
  }
)
```

```shell
db.users.updateMany(
  {},
  {
    $rename: {
      name: "full_name"
    }
  }
)
```

```shell
db.users.deleteOne({ age: 67 })
```

```shell
db.users.bulkWrite(
  [
    {
        insertOne: {
          document: { name: "Иван Николаевич", age: 24 }
        }
    },
    {
        deleteOne: {
          filter: {
            full_name: "Another user"
          }
        }
    }
  ]
)
```

```shell
db.users.update(
  { full_name: "Степан Богданович" },
  {
    $set: {
      posts: [
        { title: "Хорошая статья", text: "Текст сообщения" },
        { title: "Отлична статья", text: "Еще текст сообщения" },
        { title: "Прекрасна статья", text: "Опять текст сообщения" },
        { title: "Средняя статейка", text: "Краткое описание сообщения" },
      ]
    }
  }
)
```

```shell
db.users.findOne( { full_name: "Степан Богданович" }, { posts: 1 })
```

```shell
db.users.find( 
    {
      posts: {
        $elemMatch: {
          title: "Хорошая статья"
        }
      }
    }
)
```

```shell
db.users.find( 
    {
      posts: {
        $elemMatch: {
          title: /роша/ 
        }
      }
    }
)
```


* `title: /роша/ # Like '%роша%'`
* `title: /^роша/ # Like 'роша%'`
* `title: /роша$/ # Like '%роша'`

```shell
db.users.find({ posts: { $exists: true }})
```










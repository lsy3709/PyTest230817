use("blog2");
db.createCollection("users");
for(i = 1; i <= 10; i++) {
    db.users.insertOne(
        {name : {first : "Jinho" + i, last : "Jang"}, email : "jjh0" + i + "@naver.com", 
        password : "jjh1234" + i, Tags : ["aa" + i, "bb" + i, "cc" + i, "dd" + i], nickname : "cocozzang" + i, date : new Date()}
    );
}

use("blog2");
db.users.find({}, {"_id" : false, "password" : false});
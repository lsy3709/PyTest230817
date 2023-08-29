db.rating.aggregate([
    {
      $match: {
        user_id: { $lte: 6 },
      },
    },
    {
      $group: {
        _id: "$rating",
        count: {
          $sum: 1,
        },
      },
    },
  ]);

// 샘플 데이터베이스 특정 디비 선택 안하면 기본으로 -> use("test")
// 샘플디비 공공데이터 각 지역별 지출 보고, 가져오기

// 구조 db.rating.aggregate([ {각 스테이지 1}, {각 스테이지 2}, {각 스테이지 3} ])
db.rating.aggregate([
    {
      // 각 스테이즈 1
      $match: {
        user_id: { $lte: 6 },
      },
    },
    //각 스테이지 별로 연산된 결과 데이터가 또 다른 스테이즈의 입력값으로 사용이 됨 
    //=> 파이프라인
    {
      // 각 스테이지 2, 중요
      $group: {
        _id: "$rating",
        count: {
          $sum: 1,
        },
      },
    },
  ])

  // 기본 $project 연산자 예시
  db.rating.aggregate([
    {
      $project: {_id:0, rating:1}
    }
  ]);

  // 새로운 필드 추가
  db.rating.aggregate([
    {
      $project: {_id:0, rating:1, hi:"new field"}
    }
  ]);

  // multiply 새 필드 추가함
  db.rating.aggregate([
    {
      $project: {_id:0, multiply : {
    $multiply : ["$_id", "$user_id"]
  }}
    }
  ]);

  // 그룹 예시
  db.rating.aggregate([
    {
  $group: {
    _id: "$rating", count: {$sum: 1}
  }
    }
  ]);

  // 평점 4 이상인 사용자의 id 들을 배열의 형태로 정리하도록 명령.
  db.rating.aggregate([
    {
      $match: {
        rating: {
          $gte: 4,
        },
      },
    }, //스테이지 중하나인  match : 조건
    {
      $group: {
        _id: "$rating",
        user_ids: {
          $push: "$user_id", // 배열로 만들기.
        },
      },
    },
  ]);


//----------------------------------------------------

db.local.aggregate([
    {
    $match:
    {sub_category: "의회비"}
    },
    {
    $group : {
    _id: "$city_or_province",
    max_expense: {
    $max: "$former_expense"
    }
    }
    
    },
    { $sort: {
        max_expense: -1
    }}
    
    ]);

  
  



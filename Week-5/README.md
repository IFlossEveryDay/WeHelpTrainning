# 要求三

* 新增⼀筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。

   ```sql
        insert into member
            (name, username, password, follower_count) 
            value("John", "test", "test", 10);
  
        insert into member
            (name, username, password, follower_count)
            value("Mike", "mike123", "mike123", 20);

        insert into member
            (name, username, password, follower_count)
            value("Jim", "jim123", "jim123", 50);

        insert into member
            (name, username, password, follower_count)
            value("Maggie", "maggie123", "maggie123", 500);

        insert into member
            (name, username, password, follower_count)
            value("Amy", "amy123", "amy123", 5);
    ```

----

* 取得所有在 member 資料表中的會員資料

  ``` sql
  select * from member
  ```

![select * from member](/imgs/%E4%BD%BF%E7%94%A8select%E6%8C%87%E4%BB%A4%E5%8F%96%E5%BE%97%E6%89%80%E6%9C%89%E5%9C%A8%20member%20%E8%B3%87%E6%96%99%E8%A1%A8%E4%B8%AD%E7%9A%84%E6%9C%83%E5%93%A1%E8%B3%87%E6%96%99.png)

----

* 取得所有在 member 資料表中的會員資料，並按照 time 欄位，由
近到遠排序。

    ``` sql
        select * from member order by time desc;
    ```

    ![order by time desc](/imgs/time由近到遠.png)

----

* 取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。

    ```sql
        select * from member order by time desc limit 1, 3;
    ```

    ![limit1,3](/imgs/2-4筆資料.png)

----

* 取得欄位 username 是 test 的會員資料。
  
    ```sql
        select * from member where username="test";
    ```

    ![username=test](/imgs/username.png)

----

  
* 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
  
    
    ```sql
        select * from member 
            where username="test" and password="test";
    ```
    ![username and password = test](/imgs/username%20&&%20password.png)

----

* 更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。

    ```sql
        set sql_safe_updates=0;

        update member set name = "test2" 
            where username = "test";
    ```
    ![change to test2](imgs/test2.png)

----

# 要求四

* 取得 member 資料表中，總共有幾筆資料。

    ```sql
        select count(*) from member;
    ```
    ![how many members](/imgs/共有幾位會員.png)

----

* 取得 member 資料表中，所有會員 follower_count 欄位的總和。

    ```sql
        select sum(follower_count) from member;
    ```
    
    ![follower count](/imgs/總和.png)

----

* 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

    ```sql
        select avg(follower_count) from member;
    ```

    ![avg follower count](/imgs/截圖%202022-10-17%20下午6.19.57.png)

----

# 要求五

* 在資料庫中，建立新資料表紀錄留⾔資訊，取名字為 message 。資料表中必須包含以下欄位設定：

    ```sql
        create table message(
            id bigint primary key auto_increment,
            member_id bigint not null,
            content varchar(255) not null,
            like_count int unsigned not null default 0,
            time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    ```

    ![create table message](/imgs/要求五之一.png)

----

* member中多增加幾個 username 為 test 的使用者

    ```sql
        insert into member 
            (name, username, password, follower_count) 
            values ("Jush", "test", "test", 30);

        insert into member 
            (name, username, password, follower_count) 
            values ("Amber", "test", "test", 70);

        insert into member 
            (name, username, password, follower_count) 
            values ("Patty", "test", "test", 2);
    ```
    ![new user](/imgs/新增username為test的只用者.png)

----

* 新增message;

    ```sql
        nsert into message 
            (member_id, content, like_count) 
            values(1, "安安", 15);

        insert into message 
            (member_id, content, like_count) 
            values(2, "你好", 3);

        insert into message 
            (member_id, content, like_count) 
            values(3, "哈哈", 50);

        insert into message 
            (member_id, content, like_count) 
            values(4, "讚", 20);

        insert into message 
            (member_id, content, like_count) 
            values(5, "讚讚", 10);

        insert into message 
            (member_id, content, like_count) 
            values(6, "呵呵", 10);

        insert into message 
            (member_id, content, like_count) 
            values(7, "嘻嘻", 90);

        insert into message 
            (member_id, content, like_count) 
            values(8, "UU", 40);
    ```
    ![new message value](/imgs/新增message.png)

* 取得所有留⾔，結果須包含留⾔者會員的姓名。

    ```sql
        select member.name, 
            message.content, 
            like_count 
            from member inner join message on 
                member.id = message.member_id;
    ```
    ![all messages](/imgs/取得所有包含姓名的留言.png)

----

* foreign key 建立關聯性

    ```sql
        alter table message 
        add foreign key
        (member_id) references 
        member(id);
    ```

----

* 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。

    ```sql
        select member.name, 
            member.username, 
            message.content, 
            like_count 
            from member inner join message on 
            member.username = "test"
            and member.id = message.member_id;
    ```
    ![all test message](/imgs/username為%20test%20的留言資料.png)

----

* 將username 建立index

    ```sql
        alter table member 
        add index username_index(username);
    ```

----

* 取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數

    ```sql
        select avg(like_count) 
            from message inner join member on member.username = "test" and
            member.id = message.member_id;
    ```
    ![avg like count](/imgs/username為%20test%20的平均讚數.png)

<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<%@ page import="youngmin.web.user.UserDAO" %>
<%@ page import="youngmin.web.user.User" %>
<%@ page import="java.util.ArrayList" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="../../css/bootstrap.css">
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="../../js/bootstrap.js"></script>
    <script type="text/javascript">
        function checkAll()
        {
            var parentCheckbox = document.getElementById("checkAll").checked;
            var checkboxList = document.getElementsByName("td_check");
            for (var i = 0; i < checkboxList.length; i++)
            {
                checkboxList[i].checked = parentCheckbox;
            }
        }

        function linkId(self, userId)
        {
            if (self.checked === true) self.value = userId;
            else self.value = "";
        }

        function deleteCheckUser(event)
        {
            var checkBoxList = document.getElementsByName("td_check");
            for (var i = 0; i < checkBoxList.length; i++)
            {
                if (checkBoxList[i].value !== "")

            }
        }
    </script>

    <title>영민이의 JSP 웹사이트</title>
</head>
<body>

<nav class="navbar navbar-default">
    <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed"
                data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"
                aria-expanded="false">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="../main.jsp">영민이의 JSP 웹사이트(관리자 페이지)</a>
    </div>
    <div class="collapse navbar-collapse" id="#bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
                <a href="#" class="dropdown-toggle"
                   data-toggle="dropdown" role="button" aria-haspopup="true"
                   aria-expanded="false">관리자 메뉴
                    <span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li class="active"><a href="#">회원관리</a></li>
                    <li><a href="bbsAdmin.jsp">게시판관리</a></li>
                </ul>
            </li>
        </ul>
    </div>
</nav>

<div class="container">
    <div class="row">
<%--            <form method="post" action="../login_Action.jsp">--%>
<%--                <h3 style="text-align: center;">로그인 화면</h3>--%>
<%--                <div class="form-group">--%>
<%--                    <input type="text" class="form-control" name="id" placeholder="아이디" maxlength="15">--%>
<%--                </div>--%>
<%--                <div class="form-group">--%>
<%--                    <input type="password" class="form-control" name="password" placeholder="비밀번호" maxlength="15">--%>
<%--                </div>--%>
<%--                <input type="submit" class="btn btn-primary form-control" value="로그인">--%>
<%--            </form>--%>
        <table class="table table-striped" style="text-align: center; border: 1px solid black;">
            <thead>
                <tr>
                    <th style="text-align: center"><input type="checkbox" id="checkAll" onclick="checkAll()"/></th>
                    <th style="text-align: center">아이디</th>
                    <th style="text-align: center">비밀번호</th>
                    <th style="text-align: center">이름</th>
                    <th style="text-align: center">나이</th>
                    <th style="text-align: center">이메일</th>
                    <th style="text-align: center">전화번호</th>
                </tr>
            </thead>
            <tbody>
<%
    UserDAO userDAO = new UserDAO();
    ArrayList<User> userList = userDAO.getUserList();
    for (User userData:userList)
    {
%>
                <tr>
                    <td><input type="checkbox" id="deleteCheck" name="td_check" value="" onchange="linkId(this, "<%= userData.getId() %>")"/></td>
                    <td><%= userData.getId() %></td>
                    <td><%= userData.getPassword() %></td>
                    <td><%= userData.getName() %></td>
                    <td><%= userData.getAge() %></td>
                    <td><%= userData.getEmail() %></td>
                    <td><%= userData.getPhoneNumber() %></td>
                </tr>
<%
    }
%>
            </tbody>
        </table>
        <input type="button" id="userDeleteButton" name="deleteButton" class="btn btn-danger" value="삭제"/>
    </div>
</div>
</body>
</html>
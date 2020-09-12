<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="../../css/bootstrap.css">
    <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script src="../../js/bootstrap.js"></script>

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
        <ul class="nav navbar-nav">
            <%--            <li><a href="main.jsp">메인</a></li>--%>
            <%--            <li><a href="bbs.jsp">게시판</a></li>--%>
        </ul>
        <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
                <a href="#" class="dropdown-toggle"
                   data-toggle="dropdown" role="button" aria-haspopup="true"
                   aria-expanded="false">관리자 메뉴
                    <span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li><a href="memberAdmin.jsp">회원관리</a></li>
                    <li class="active"><a href="#">게시판관리</a></li>
                </ul>
            </li>
        </ul>
    </div>
</nav>

<div class="container">
    <div class="col-lg-4"></div>
    <div class="col-lg-4">
        <div class="jumbotron">
            <form method="post" action="../login_Action.jsp">
                <h3 style="text-align: center;">로그인 화면</h3>
                <div class="form-group">
                    <input type="text" class="form-control" name="id" placeholder="아이디" maxlength="15">
                </div>
                <div class="form-group">
                    <input type="password" class="form-control" name="password" placeholder="비밀번호" maxlength="15">
                </div>
                <input type="submit" class="btn btn-primary form-control" value="로그인">
            </form>
        </div>
    </div>
    <div class="col-lg-4"></div>
</div>
</body>
</html>
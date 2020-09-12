<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-16
  Time: 오전 2:20
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" language="java" %>
<html>
<head>
    <%@include file="file_header.jsp" %>
    <title>회원 탈퇴</title>
</head>
<body>
<%@include file="page_header.jsp" %>
<%--<%--%>
<%--    // 로그인 상태에 따라 화면 디자인 별도 처리를 위해 세션을 통해 로그인 검사할 수 있도록 세션값 받아옴.--%>
<%--    String userID = null;--%>
<%--    if (session.getAttribute("userID") != null)--%>
<%--        userID = session.getAttribute("userID").toString();--%>
<%--%>--%>
<%--<nav class="navbar navbar-default navbar-fixed-top">--%>
<%--    <div class="navbar-header">--%>
<%--        <button type="button" class="navbar-toggle collapsed"--%>
<%--                data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"--%>
<%--                aria-expanded="false">--%>
<%--            <span class="icon-bar"></span>--%>
<%--            <span class="icon-bar"></span>--%>
<%--            <span class="icon-bar"></span>--%>
<%--        </button>--%>
<%--        <a class="navbar-brand" href="main.jsp"><strong>영민이의 영화 채널</strong></a>--%>
<%--    </div>--%>
<%--    <div class="collapse navbar-collapse" id="#bs-example-navbar-collapse-1">--%>
<%--        <ul class="nav navbar-nav">--%>
<%--            <li class="active"><a href="main.jsp">메인 화면</a></li>--%>
<%--            <li><a href="movie_research.jsp">영화 검색</a></li>--%>
<%--            <li><a href="review_list.jsp">리뷰 목록</a></li>--%>
<%--            <li><a href="review_write.jsp">리뷰 쓰기</a></li>--%>
<%--            <li><a href="wishlist.jsp">위시리스트</a></li>--%>
<%--        </ul>--%>
<%--        <%--%>
<%--            if (userID == null)--%>
<%--            {--%>
<%--        %>--%>
<%--        <ul class="nav navbar-nav navbar-right">--%>
<%--            <li class="dropdown">--%>
<%--                <a href="#" class="dropdown-toggle"--%>
<%--                   data-toggle="dropdown" role="button" aria-haspopup="true"--%>
<%--                   aria-expanded="false">접속하기--%>
<%--                    <span class="caret"></span></a>--%>
<%--                <ul class="dropdown-menu">--%>
<%--                    <li><a href="join.jsp">회원가입</a></li>--%>
<%--                </ul>--%>
<%--            </li>--%>
<%--        </ul>--%>
<%--        <%--%>
<%--        }--%>
<%--        else--%>
<%--        {--%>
<%--        %>--%>
<%--        <ul class="nav navbar-nav navbar-right">--%>
<%--            <li class="dropdown">--%>
<%--                <a href="#" class="dropdown-toggle"--%>
<%--                   data-toggle="dropdown" role="button" aria-haspopup="true"--%>
<%--                   aria-expanded="false">계정관리--%>
<%--                    <span class="caret"></span></a>--%>
<%--                <ul class="dropdown-menu">--%>
<%--                    <li><a href="logout_Action.jsp">로그아웃</a></li>--%>
<%--                    <li><a href="userinfo_update.jsp">계정정보 수정</a></li>--%>
<%--                    <li><a href="withdrawal.jsp">회원탈퇴</a></li>--%>
<%--                </ul>--%>
<%--            </li>--%>
<%--        </ul>--%>
<%--        <%--%>
<%--            }--%>
<%--        %>--%>
<%--    </div>--%>
<%--</nav>--%>

<div class="container">
    <div class="col-lg-4"></div>
    <div class="col-lg-4">
        <div class="jumbotron">
            <form name="withdrawalForm" method="post" action="withdrawal_Action.jsp">
                <h3 style="text-align: center;">회원 탈퇴</h3>
                <div class="label label-default">
                    <label>비밀번호를 입력해주세요.</label>
                </div>
                <div class="form-group">
                    <input type="password" class="form-control" id="withdrawal_userPW" name="userPW" placeholder="비밀번호" maxlength="15"/>
                </div>
                <div class="form-group">
                    <input type="submit" class="btn btn-primary form-control" value="회원탈퇴">
                </div>
            </form>
        </div>
    </div>
    <div class="col-lg-4"></div>
</div>

<%@include file="page_footer.jsp" %>
</body>
</html>

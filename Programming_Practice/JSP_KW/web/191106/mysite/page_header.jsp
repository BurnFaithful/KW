<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-21
  Time: 오후 6:28
  To change this template use File | Settings | File Templates.
--%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ page language="java" contentType="text/html;charset=UTF-8" pageEncoding="UTF-8" %>
<%--로그인 상태에 따라 화면 디자인 별도 처리를 위해 세션을 통해 로그인 검사할 수 있도록 세션값 받아옴.--%>
<c:set var="userID" value="${sessionScope.userID}"/>

<div id="page-header">
    <nav class="navbar navbar-default">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed"
                    data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"
                    aria-expanded="false">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="main.jsp"><strong>영민이의 영화 채널</strong></a>
        </div>
        <div class="collapse navbar-collapse" id="#bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li id="main-page-nav"><a href="main.jsp?pageName=Main">메인 화면</a></li>
                <li id="movieresearch-page-nav"><a href="movie_research.jsp?pageName=Movie_Research">영화 검색</a></li>
                <li id="reviewlist-page-nav"><a href="review_list.jsp?pageName=Review_List">리뷰 목록</a></li>
                <li id="reviewwrite-page-nav"><a href="review_write.jsp?pageName=Review_Write">리뷰 쓰기</a></li>
                <li id="wishlist-page-nav"><a href="wishlist.jsp?pageName=Wishlist">위시리스트</a></li>
            </ul>
            <c:choose>
                <c:when test="${empty userID}">
            <ul class="nav navbar-nav navbar-right">
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle"
                       data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">접속하기
                        <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="join.jsp">회원가입</a></li>
                    </ul>
                </li>
            </ul>
                </c:when>
                <c:otherwise>
            <ul class="nav navbar-nav navbar-right">
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle"
                       data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">계정관리
                        <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="logout_Action.jsp">로그아웃</a></li>
                        <li><a href="userinfo_update.jsp">계정정보 수정</a></li>
                        <li><a href="withdrawal.jsp">회원탈퇴</a></li>
                    </ul>
                </li>
            </ul>
                </c:otherwise>
            </c:choose>
        </div>
    </nav>
</div>

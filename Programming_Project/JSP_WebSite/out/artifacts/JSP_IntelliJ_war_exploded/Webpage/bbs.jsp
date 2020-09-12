<%@ page language="java" contentType="text/html; charset=UTF-8"
		 pageEncoding="UTF-8"%>
<%@ page import="youngmin.web.bbs.BbsDAO, youngmin.web.bbs.Bbs" %>
<%@ page import="java.util.ArrayList" %>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="../css/bootstrap.css">
	<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
	<script src="../js/bootstrap.js"></script>

	<title>영민이의 JSP 웹사이트</title>
	<style type="text/css">
		a, a:hover {
			color: black;
			text-decoration: none;
		}
	</style>
</head>
<body>
<%
	String userId = null;
	if (session.getAttribute("id") != null)
	{
		userId = (String)session.getAttribute("id");
	}
	int pageNum = 1;
	if (request.getParameter("pageNum") != null) pageNum = Integer.parseInt(request.getParameter("pageNum"));
%>
<nav class="navbar navbar-default">
	<div class="navbar-header">
		<button type="button" class="navbar-toggle collapsed"
				data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"
				aria-expanded="false">
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
			<span class="icon-bar"></span>
		</button>
		<a class="navbar-brand" href="main.jsp">영민이의 JSP 웹사이트</a>
	</div>
	<div class="collapse navbar-collapse" id="#bs-example-navbar-collapse-1">
		<ul class="nav navbar-nav">
			<li><a href="main.jsp">메인</a></li>
			<li class="active"><a href="bbs.jsp">게시판</a></li>
		</ul>
		<%
			if (userId == null) {
		%>
		<ul class="nav navbar-nav navbar-right">
			<li class="dropdown">
				<a href="#" class="dropdown-toggle"
				   data-toggle="dropdown" role="button" aria-haspopup="true"
				   aria-expanded="false">접속하기
					<span class="caret"></span></a>
				<ul class="dropdown-menu">
					<li class="active"><a href="login.jsp">로그인</a></li>
					<li><a href="join.jsp">회원가입</a></li>
				</ul>
			</li>
		</ul>
		<%
		} else {
		%>
		<ul class="nav navbar-nav navbar-right">
			<li class="dropdown">
				<a href="#" class="dropdown-toggle"
				   data-toggle="dropdown" role="button" aria-haspopup="true"
				   aria-expanded="false">회원관리
					<span class="caret"></span></a>
				<ul class="dropdown-menu">
					<li><a href="logout_Action.jsp">로그아웃</a></li>
				</ul>
			</li>
		</ul>
		<%
			}
		%>
	</div>
</nav>
<div class="container">
	<div class="row">
		<table class="table table-striped" style="text-align: center; border: 1px solid #dddddd">
			<thead>
				<tr>
					<th style="background-color: #eeeeee; text-align: center;">번호</th>
					<th style="background-color: #eeeeee; text-align: center;">제목</th>
					<th style="background-color: #eeeeee; text-align: center;">작성자</th>
					<th style="background-color: #eeeeee; text-align: center;">작성일</th>
				</tr>
			</thead>
			<tbody>
				<%
					BbsDAO bbsDAO = new BbsDAO();
					ArrayList<Bbs> list = bbsDAO.getList(pageNum);
					for (Bbs bbsData:list)
					{
				%>
				<tr>
					<td><%= bbsData.getBbsID() %></td>
					<td><a href="view.jsp?bbsId=<%= bbsData.getBbsID() %>"><%= bbsData.getBbsTitle() %></a></td>
					<td><%= bbsData.getUserID() %></td>
					<td><%= bbsData.getBbsDate().substring(0, 11) +
					 bbsData.getBbsDate().substring(11, 13) + "시 " +
					 bbsData.getBbsDate().substring(14, 16) + "분" %></td>
				</tr>
				<%
				 }
				%>
			</tbody>
		</table>
		<%
			if (pageNum != 1) {
		%>
			<a href="bbs.jsp?pageNum=<%= pageNum - 1 %>" class="btn btn-success btn-arrow-left">이전 페이지</a>
		<%
			}
			if (bbsDAO.nextPage(pageNum + 1)) {
		%>
			<a href="bbs.jsp?pageNum=<%= pageNum + 1 %>" class="btn btn-success btn-arrow-right">다음 페이지</a>
		<%
			}
		%>
		<a href="write.jsp" class="btn btn-primary pull-right">글쓰기</a>
	</div>
</div>
</body>
</html>
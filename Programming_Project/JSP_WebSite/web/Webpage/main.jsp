<%@ page language="java" contentType="text/html; charset=UTF-8"
		 pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="../css/bootstrap.css">
	<link rel="stylesheet" href="../css/youngmin_jumbotron.css">
	<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
	<script src="../js/bootstrap.js"></script>

	<title>영민이의 JSP 웹사이트</title>
</head>
<body>
	<%
		// 로그인 상태에 따라 화면 디자인 별도 처리를 위해 세션을 통해 로그인 검사할 수 있도록 세션값 받아옴.
		String userId = null;
		if (session.getAttribute("id") != null)
		{
			userId = (String)session.getAttribute("id");
		}
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
			<li class="active"><a href="main.jsp">메인</a></li>
			<li><a href="bbs.jsp">게시판</a></li>
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
					<li><a href="login.jsp">로그인</a></li>
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
				   aria-expanded="false">계정관리
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
	<div class="jumbotron">
		<div class="container">
			<h1>영민이의 게시판 연습 사이트</h1>
			<p>이 웹사이트는 부트스트랩으로 만든 영민이의 JSP 게시판 연습 사이트입니다.</p>
			<a class="btn btn-primary btn-pull" href="#" role="button">자세히 알아보기</a>
		</div>
	</div>
</div>
<div class="container">
	<div id="myCarousel" class="carousel slide" data-ride="carousel">
		<ol class="carousel-indicators">
			<li data-target="#myCarousel" data-slide-to="0" class="active"></li>
			<li data-target="#myCarousel" data-slide-to="1"></li>
			<li data-target="#myCarousel" data-slide-to="2"></li>
			<li data-target="#myCarousel" data-slide-to="3"></li>
			<li data-target="#myCarousel" data-slide-to="4"></li>
			<li data-target="#myCarousel" data-slide-to="5"></li>
			<li data-target="#myCarousel" data-slide-to="6"></li>
			<li data-target="#myCarousel" data-slide-to="7"></li>
			<li data-target="#myCarousel" data-slide-to="8"></li>
		</ol>
		<div class="carousel-inner">
			<div class="item active">
				<img src="../Images/Tristana.jpg">
			</div>
			<div class="item">
				<img src="../Images/Ashe.jpg">
			</div>
			<div class="item">
				<img src="../Images/Sivir.jpg">
			</div>
			<div class="item">
				<img src="../Images/Varus.jpg">
			</div>
			<div class="item">
				<img src="../Images/Jhin.jpg">
			</div>
			<div class="item">
				<img src="../Images/Lucian.jpg">
			</div>
			<div class="item">
				<img src="../Images/Kaisa.jpg">
			</div>
			<div class="item">
				<img src="../Images/MissFortune.jpg">
			</div>
			<div class="item">
				<img src="../Images/Xayah.jpg">
			</div>
		</div>
		<a class="left carousel-control" href="#myCarousel" data-slide="prev">
			<span class="glyphicon glyphicon-chevron-left"></span>
		</a>
		<a class="right carousel-control" href="#myCarousel" data-slide="next">
			<span class="glyphicon glyphicon-chevron-right"></span>
		</a>
	</div>
</div>
</body>
</html>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="../css/bootstrap.css">
	<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
	<script src="../js/bootstrap.js"></script>
	<script type="text/javascript">
		function validate()
		{ // 클라이언트 폼에서 입력해야 할 값들이 유효하게 입력되었는지 검사
			var id = document.getElementById("id");
			var pw = document.getElementById("password");
			var name = document.getElementById("name");
			var age = document.getElementById("age");
			var email = document.getElementById("email");
			var phoneNumber = document.getElementById("phoneNumber");

			if (!id.value || !pw.value || !name.value || !age.value || !email.value || !phoneNumber.value)
			{
				alert("입력하지 않은 사항이 있습니다.");
				return false;
			}
			return true;
		}
	</script>

	<title>영민이의 영화 채널 - 회원가입</title>
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
				<a class="navbar-brand" href="main.jsp">영민이의 JSP 웹사이트</a>
		</div>
		<div class="collapse navbar-collapse" id="#bs-example-navbar-collapse-1">
			<ul class="nav navbar-nav">
				<li><a href="main.jsp">메인</a></li>
				<li><a href="bbs.jsp">게시판</a></li>
			</ul>
			<ul class="nav navbar-nav navbar-right">
				<li class="dropdown">
					<a href="#" class="dropdown-toggle"
					data-toggle="dropdown" role="button" aria-haspopup="true"
					aria-expanded="false">접속하기
					<span class="caret"></span></a>
					<ul class="dropdown-menu">
						<li><a href="login.jsp">로그인</a></li>
						<li class="active"><a href="join.jsp">회원가입</a></li>
					</ul>
				</li>
			</ul>
		</div>
	</nav>
	
	<div class="container">
		<div class="col-lg-4"></div>
		<div class="col-lg-4">
			<div class="jumbotron">
				<form name="joinForm" method="post" onsubmit="return validate();" action="join_Action.jsp">
					<h3 style="text-align: center;">회원가입 화면</h3>
					<div class="form-group">
						<input type="text" class="form-control" id="id" name="id" placeholder="아이디" maxlength="15">
					</div>
					<div class="form-group">
						<input type="password" class="form-control" id="password" name="password" placeholder="비밀번호" maxlength="15">
					</div>
					<div class="form-group">
						<input type="text" class="form-control" id="name" name="name" placeholder="이름" maxlength="15">
					</div>
					<div class="form-group">
						<input type="text" class="form-control" id="age" name="age" placeholder="나이" maxlength="3">
					</div>
					<div class="form-group">
						<input type="text" class="form-control" id="email" name="email" placeholder="이메일" maxlength="30">
					</div>
					<div class="form-group">
						<input type="text" class="form-control" id="phoneNumber" name="phoneNumber" placeholder="전화번호" value="" maxlength="20">
					</div>
					<input type="submit" class="btn btn-primary form-control" value="회원가입">
				</form>
			</div>
		</div>
		<div class="col-lg-4"></div>
	</div>
</body>
</html>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="youngmin.web.user.UserDAO" %>

<% request.setCharacterEncoding("UTF-8"); %>
<jsp:useBean id="user" class="youngmin.web.user.User" scope="page"/>
<jsp:setProperty name="user" property="id"/>
<jsp:setProperty name="user" property="password"/>

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Login_Action</title>
	<script type="text/javascript">
		function checkSession(sessionValue)
		{
			if (sessionValue != null) // 세션 검사
			{
				alert("이미 로그인이 되어있습니다.");
				location.href = 'main.jsp';
			}
		}

		function checkLogin(result, userId)
		{
			switch (result)
			{
				case 1:
					if ("<%= user.getId() %>" === "admin")
					{
						alert("관리자 계정 로그인. 관리자 페이지로 이동.");
						location.href = 'admin/admin.jsp';
					}
					else
					{
						alert("로그인 성공");
						location.href = 'main.jsp';
					}
					break;
				case 0:
					alert("로그인 실패. 비밀번호가 틀림.");
					break;
				case -1:
					alert("로그인 실패. 아이디가 없거나 일치하지 않음.");
					break;
				case -2:
					alert("데이터베이스 오류");
					break;
				default:
					alert("알 수 없는 오류");
					break;
			}
		}
	</script>
</head>
<body>
<%
	String userId = null;
	if (session.getAttribute("id") != null)
		userId = (String)session.getAttribute("id");
%>
	<script>
		checkSession(<%= userId %>);
	</script>
<%
	UserDAO userDAO = new UserDAO();
	// 안 좋은 쿼리문 작성 → SQL Injection에 뚫림.
	//String query = "SELECT id, password FROM USER WHERE id=" + userId + " AND password=" + userPw;
	int loginResult = userDAO.login(user.getId(), user.getPassword()); // DB를 통해 로그인 처리
	if (loginResult == 1) // 로그인에 성공하면 세션에 id 저장
	{
		userId = user.getId();
		session.setAttribute("id", user.getId());
	}
%>
	<script>
		checkLogin(<%= loginResult %>, "<%= userId %>");
	</script>
</body>
</html>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<%@ page import="youngmin.web.user.UserDAO" %>
<% request.setCharacterEncoding("UTF-8"); %>
<jsp:useBean id="user" class="youngmin.web.user.User" scope="page" />
<jsp:setProperty name="user" property="*" />

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Join_Action</title>
	<script type="text/javascript">
		function checkJoin(result)
		{
			if (result === -1)
			{
				alert("이미 존재하는 아이디입니다.");
				history.back();
			}
			else
			{
				<% session.setAttribute("id", user.getId()); %>
				alert("회원가입 성공.");
				location.href = "main.jsp";
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
		int result = userDAO.join(user);
	%>
		<script>
			checkJoin(<%= result %>);
		</script>
</body>
</html>
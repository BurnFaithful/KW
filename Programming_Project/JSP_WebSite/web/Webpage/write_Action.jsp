<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<%@ page import="youngmin.web.bbs.BbsDAO" %>

<% request.setCharacterEncoding("UTF-8"); %>
<jsp:useBean id="bbs" class="youngmin.web.bbs.Bbs" scope="page"/>
<jsp:setProperty name="bbs" property="bbsTitle"/>
<jsp:setProperty name="bbs" property="bbsContent"/>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <script type="text/javascript">
        function checkSession(sessionValue)
        {
            if (sessionValue == null)
            {
                alert("로그인이 필요합니다.");
                location.href = 'login.jsp';
            }
        }

        function checkWrite(result)
        {
            if (result === -1)
                alert("글쓰기에 실패하였습니다.");
            else
                location.href = 'bbs.jsp';
        }
    </script>

    <title>Write_Action</title>
</head>
<body>
<%
    String userId = null;
    if (session.getAttribute("id") != null) userId = (String)session.getAttribute("id");
%>
    <script>
        checkSession(<%= userId %>);
    </script>
<%
    BbsDAO bbsDAO = new BbsDAO();
    int result = bbsDAO.write(bbs.getBbsTitle(), userId, bbs.getBbsContent());
%>
    <script>
        checkWrite(<%= result %>);
    </script>
</body>
</html>
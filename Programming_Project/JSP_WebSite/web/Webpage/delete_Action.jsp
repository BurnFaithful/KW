<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<%@ page import="youngmin.web.bbs.BbsDAO, youngmin.web.bbs.Bbs" %>

<% request.setCharacterEncoding("UTF-8"); %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Delete_Action</title>
    <script type="text/javascript">
        function checkSession(sessionValue)
        {
            if (sessionValue == null)
            {
                alert("로그인이 필요합니다.");
                location.href = 'login.jsp';
            }
        }

        function checkAuthority(id)
        {
            if (id == null)
            {
                alert("권한이 없습니다!");
                location.href = "bbs.jsp";
            }
        }

        function checkDeleteResult(result)
        {
            if (result === -1)
                alert("글 삭제에 실패했습니다.");
            else
                location.href = "bbs.jsp";
        }
    </script>
</head>
<body>
<%
    String userId = null;
    if (session.getAttribute("id") != null) userId = (String)session.getAttribute("id");
%>
    <script>checkSession(<%= userId %>)</script>

<%
    int bbsId = 0;
    if (request.getParameter("bbsId") != null)
        bbsId = Integer.parseInt(request.getParameter("bbsId"));
%>
    <script>checkAuthority(<%= bbsId %>)</script>
<%
    Bbs bbs = new BbsDAO().getBbs(bbsId);
    assert userId != null;
    boolean checkId = userId.equals(bbs.getUserID());
%>
    <script>checkAuthority(checkId);</script>
<%
    BbsDAO bbsDAO = new BbsDAO();
    int result = bbsDAO.delete(bbsId);
%>
    <script>checkDeleteResult(<%= result %>);</script>
</body>
</html>
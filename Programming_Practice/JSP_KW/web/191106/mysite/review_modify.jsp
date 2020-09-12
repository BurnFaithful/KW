<%@ page import="youngmin.bbs.ReviewbbsDTO" %>
<%@ page import="youngmin.bbs.ReviewbbsDAO" %><%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-20
  Time: 오후 1:30
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <%@include file="file_header.jsp" %>

    <title>리뷰 수정</title>
</head>
<body>
<%@include file="page_header.jsp" %>
<%
    // 로그인 상태에 따라 화면 디자인 별도 처리를 위해 세션을 통해 로그인 검사할 수 있도록 세션값 받아옴.
    String userID = null;
    if (session.getAttribute("userID") != null)
        userID = session.getAttribute("userID").toString();

    int reviewID = 0;
    if (request.getParameter("reviewID") != null)
        reviewID = Integer.parseInt(request.getParameter("reviewID"));

    ReviewbbsDTO reviewbbs = null;
    if (reviewID != 0)
    {
        reviewbbs = new ReviewbbsDAO().getBBSInfo(reviewID);
    }
%>
<%--<c:set var="reviewID" value="${param.reviewID+0}"/>--%>
<%--<fmt:formatNumber value--%>

<div class="container">
    <div class="row">
        <form method="post" action="review_modify_Action.jsp?reviewID=<%= reviewID %>">
            <table class="table table-striped" style="text-align: center; border: 1px solid #dddddd">
                <thead>
                <tr>
                    <th colspan="2" style="background-color:#eeeeee; text-align: center;">리뷰 쓰기</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td><input type="text" class="form-control" placeholder="영화 제목" id="review_bbsTitle" name="reviewTitle" maxlength="50" value="<%= reviewbbs.getReviewTitle() %>"></td>
                </tr>
                <tr>
                    <td><textarea class="form-control" placeholder="리뷰 작성해주세요. 500자 미만." id="review_bbsContent" name="reviewContent" maxlength="500" style="height: 350px;"><%= reviewbbs.getReviewContent() %></textarea></td>
                </tr>
                </tbody>
            </table>
            <input type="submit" class="btn btn-primary pull-right" value="글 수정">
        </form>
    </div>
</div>

<%@include file="page_footer.jsp" %>
</body>
</html>

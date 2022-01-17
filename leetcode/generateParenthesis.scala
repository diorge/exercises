// https://leetcode.com/problems/generate-parentheses

object Solution {
  def generateParenthesis(n: Int): List[String] = {
    def inner(
        currently_opened: Int,
        total_opened: Int,
        closed: Int
    ): List[String] = {
      if (closed == n) {
        List()
      } else if (total_opened == n && closed == n - 1) {
        List(")")
      } else if (total_opened < n) {
        if (currently_opened == 0) {
          inner(1, total_opened + 1, closed).map("(" + _)
        } else {
          val opening =
            inner(currently_opened + 1, total_opened + 1, closed).map("(" + _)
          val closing =
            inner(currently_opened - 1, total_opened, closed + 1).map(")" + _)
          List.concat(opening, closing)
        }
      } else {
        inner(currently_opened - 1, total_opened, closed + 1).map(")" + _)
      }
    }
    inner(0, 0, 0)
  }
}

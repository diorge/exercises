// https://leetcode.com/problems/reverse-integer

import scala.math.abs
import scala.math.pow

object Solution {
  val non_neg_str = "2147483648"
  val max_str = "2147483647"

  def reverse(x: Int): Int = {
    val neg = x < 0

    def is_safe(v: String): Boolean = {
      val comp_str = if (neg) non_neg_str else max_str
      if (v.length > comp_str.length) {
        false
      } else if (v.length == comp_str.length) {
        v.zip(comp_str)
          .map({ case (a, m) =>
            if (a < m) "lt"
            else if (a == m) "eq"
            else "gt"
          })
          .reduce((curr, next) => {
            (curr, next) match {
              case ("eq", x) => x
              case (x, _)    => x
            }
          }) != "gt"
      } else {
        true
      }
    }

    val s = abs(x).toString.reverse
    if (!is_safe(s)) {
      0
    } else {
      val final_str = if (neg) "-" + s else s
      final_str.toInt
    }
  }
}

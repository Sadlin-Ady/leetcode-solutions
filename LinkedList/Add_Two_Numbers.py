def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode
        """
        curr1 = l1
        curr2 = l2
        suml = ListNode()
        result = suml
        carry = None
        while  curr1 or curr2:
            if curr1 and curr2:
                val = curr1.val + curr2.val
                if carry:
                    val += 1
                    carry = None
                if val < 10:
                    valN = ListNode(val)
                    result.next= valN
                    result = result.next
                else:
                    val = val % 10
                    valN = ListNode(val)
                    result.next = valN
                    result = result.next
                    carry = 1
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1:
                val = curr1.val
                if carry:
                    val += 1
                    carry = None
                if val < 10:
                    valN = ListNode(val)
                else:
                    val %= 10
                    valN = ListNode(val)
                    carry = 1
                result.next = valN
                result = result.next
                curr1 = curr1.next
            else:
                val = curr2.val
                if carry:
                    val += 1
                    carry = None
                if val < 10:
                    valN = ListNode(val)
                else:
                    val %= 10
                    valN = ListNode(val)
                    carry = 1
                result.next = valN
                result = result.next
                curr2 = curr2.next
        if carry:
            valN = ListNode(carry)
            result.next = valN
        return suml.next
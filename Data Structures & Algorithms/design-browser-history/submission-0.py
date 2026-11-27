class ListNode:
    def __init__(self, url, prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = ListNode(homepage)

    def visit(self, url: str) -> None:
        # we're using a doubly linked list!! self.homepage needs to be set to prev
        self.homepage.next = ListNode(url, self.homepage)
        self.homepage = self.homepage.next

    def back(self, steps: int) -> str:
        while self.homepage.prev and steps > 0:
            self.homepage = self.homepage.prev
            steps -= 1
        return self.homepage.url

    def forward(self, steps: int) -> str:
        while self.homepage.next and steps > 0:
            self.homepage = self.homepage.next
            steps -= 1
        return self.homepage.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
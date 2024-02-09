class Page:
    def __init__(self, url: str, next = None, prev = None) -> None:
        self.url = url
        self.next = next
        self.prev = prev

class Browser:
    # O(1)
    def __init__(self, url: str) -> None:
        self.curr = Page(url)
    
    # O(1)
    def get_url(self) -> str:
        return self.curr.url
    
    # O(1)
    def visit(self, url: str) -> None:
        self.curr.next = Page(url, None, self.curr)
        self.curr = self.curr.next

    # O(N)
    def back(self, steps: int) -> None:
        for _ in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
            else:
                break
    
    # O(N)
    def forward(self, steps: int) -> None:
        for _ in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
            else:
                break

def test_browser() -> None:
    # [google.com]
    browser = Browser("google.com")
    assert browser.get_url() == "google.com"

    # google.com <-> [facebook.com]
    browser.visit("facebook.com")
    assert browser.get_url() == "facebook.com"

    # [google.com] <-> facebook.com
    browser.back(1)
    assert browser.get_url() == "google.com"

    # google.com <-> [facebook.com]
    browser.forward(1)
    assert browser.get_url() == "facebook.com"

    # google.com <-> facebook.com <-> youtube.com <-> [leetcode.com]
    browser.visit("youtube.com")
    browser.visit("leetcode.com")
    assert browser.get_url() == "leetcode.com"
    
    # google.com <-> [facebook.com] <-> youtube.com <-> leetcode.com
    browser.back(2)
    assert browser.get_url() == "facebook.com"

    # google.com <-> facebook.com <-> [youtube.com] <-> leetcode.com
    browser.forward(1)
    assert browser.get_url() == "youtube.com"

    # google.com <-> facebook.com <-> youtube.com <-> [amazon.com]
    browser.visit("amazon.com")
    assert browser.get_url() == "amazon.com"

    browser = Browser("google.com")
    
    # Try to navigate back more steps than the available history
    browser.back(2)  
    
    # Try to navigate back when there's no previous URL
    browser.back(1)  
    
    # Visit "facebook.com" and then try to navigate forward more steps than the available history
    browser.visit("facebook.com")
    browser.back(1)
    browser.forward(2)

    # Visit the same URL multiple times and check navigation
    browser.visit("google.com")
    browser.visit("google.com")
    browser.back(1)
    browser.forward(1)

    print("All test cases passed!")

# Run test cases
test_browser()
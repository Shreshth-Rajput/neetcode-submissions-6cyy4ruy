class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        clean_emails = set()
        for email in emails:
            local, domain = email.split("@")

            unique_local = ""
            for c in local:
                if c == "+":
                    break
                elif c == ".":
                    continue
                else:
                    unique_local += c
            clean_emails.add(unique_local + "@" + domain)
        return len(clean_emails)
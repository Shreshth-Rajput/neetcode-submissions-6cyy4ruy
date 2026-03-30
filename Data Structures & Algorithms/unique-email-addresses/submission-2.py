class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        clean_emails = set()
        for email in emails:
            local, domain = email.split("@")
            unique_local = local.split("+")[0].replace(".", "")
       
            clean_emails.add(unique_local + "@" + domain)
        return len(clean_emails)
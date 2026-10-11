---
title: "How To Delete everything off a usb drive via cmd"
---

# How To Delete everything off a usb drive via cmd

[Download the original Word document](../word/How%20To%20Delete%20everything%20off%20a%20usb%20drive%20via%20cmd.docx)
{: .fs-2 }

{% raw %}
How To Delete everything off a usb drive via cmd

diskpart

list disk

select disk

detail disk

Clean all

create partition primary

format fs=exfat quick

assign

Exit
{% endraw %}

<%*
const subject_name = await tp.system.prompt("Subject name:"); 
const filename = await tp.system.prompt("Report filename: (pr-1)");
if (tp.file.exists("/01-Subjects/" + subject_name )) {
	const path = "/01-Subjects/" + subject_name + "/reports" 
	if (!tp.file.exists(path)) {
		await this.app.vault.createFolder(tp.obsidian.normalizePath(path))
	}
	await tp.file.rename(filename)
	await tp.file.move(path + "/" + filename)
}
%>---
title: <% filename %>
subject: "[[<% subject_name %>]]"
createdAt: <% moment(tp.file.creation_date()).format('YYYY-MM-DDTHH:mm:ss') %>
updatedAt: <% moment(tp.file.last_modified_date()).format('YYYY-MM-DDTHH:mm:ss') %>
dueDate: <% moment(tp.file.creation_date()).format('YYYY-MM-DDTHH:mm:ss') %>
tags: 
- report
---

## Title
### <% filename %>

- Author:  user
- Date: <% moment(tp.file.last_modified_date()).format('DD MMM YYYY') %>

---
# Index

- [Introduction](#Introduction)
- [Summary](#Summary)
- Chapters
	- [Chapter 1](#Chapter%202)
	- [Chapter 2](#Chapter%202)
- [Conclusions](#Conclusions)
- [Dedication](#Dedication)

---
# Introduction

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ligula augue, euismod quis mauris a, pretium pulvinar mi. Fusce lobortis placerat libero, et hendrerit ante rutrum ac. Cras vehicula varius ornare. Cras tellus metus, semper quis iaculis eu, finibus ac metus. Maecenas viverra velit sapien, a tempus nibh dapibus ac. Ut maximus finibus justo, vel molestie risus mollis tincidunt. Integer sollicitudin est at vulputate porta.
# Summary

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce et nulla interdum, bibendum nunc nec, imperdiet tellus. Nulla vitae augue at mauris scelerisque viverra finibus id odio. Pellentesque pretium mi id quam dictum, porta pellentesque tortor ornare. Phasellus a ipsum fermentum, mollis lacus non, feugiat metus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Duis in ipsum ac elit scelerisque finibus non eu metus. Phasellus tempor sodales leo eget sodales. Sed dui ante, luctus non orci eget, consectetur varius dui. Suspendisse blandit, ex vel pretium congue, augue quam tempor libero, sit amet iaculis felis mauris eget arcu. Donec vitae iaculis metus. Aliquam efficitur lacus eros. Quisque nisl ex, consectetur sed volutpat quis, vehicula sit amet nisl. Fusce faucibus odio ac faucibus lobortis. Suspendisse malesuada dolor ut dui tempus tincidunt.

Nulla facilisi. Morbi ac diam vitae neque vulputate feugiat. Proin laoreet, ante ut laoreet egestas, mi dui suscipit libero, ac laoreet tortor lectus id orci. Aenean pretium enim a diam accumsan, vel faucibus massa fermentum. In eget nisi arcu. Fusce viverra risus vitae sodales pellentesque. Phasellus iaculis quam ut tempor convallis. Nulla at imperdiet nisl. Curabitur quis feugiat nisi, vitae congue purus.

---
# Chapters
## Chapter 1

Aliquam erat volutpat. Mauris tempor bibendum est, nec venenatis eros interdum vitae. In non congue justo, imperdiet scelerisque erat. Donec nec felis in dui cursus egestas. Cras at libero convallis, mollis quam in, tincidunt sem. Cras id bibendum enim. Nam non est id ipsum pellentesque volutpat sed non purus.

```cpp
#include <iostream>

int main() {
    std::cout << "Hello World!";
    return 0;
}
```

Maecenas mollis ante nulla, nec convallis nibh lacinia eget. Maecenas purus leo, rutrum at nulla ut, viverra pretium lacus. Sed mollis elit sit amet metus interdum consequat. Pellentesque eu eleifend dolor, sit amet euismod enim. Aliquam sed dolor at magna elementum vulputate et eget ante. Nulla non iaculis turpis. Integer velit lectus, consequat sit amet pretium sed, malesuada in tortor. Nunc facilisis tellus eu imperdiet mollis. Ut vel fermentum risus. Nam ultricies dolor et magna vestibulum, ac sollicitudin leo viverra.

## Chapter 2

Nunc est lorem, pellentesque bibendum fermentum sed, venenatis in ex. Phasellus rutrum in justo eget auctor. Donec porta varius tortor id feugiat. Mauris ut bibendum mi. Nunc cursus enim diam, non molestie lorem feugiat ut. Etiam egestas maximus odio, eu fringilla enim faucibus efficitur. Maecenas aliquet ut arcu vel feugiat. Aenean eget diam eros. Sed in orci sodales, accumsan odio vel, posuere turpis. Aliquam condimentum sapien eget pretium malesuada. Vivamus interdum tempor lorem, sed efficitur turpis convallis eget. Donec aliquet tincidunt nisl, vitae bibendum tellus venenatis vel. Nulla quis arcu turpis.

$$ E=mc^2 $$

# Conclusions

Phasellus suscipit mi ac libero rutrum, at ultricies leo aliquet. Proin id convallis dui. Mauris sed ultricies purus. Vivamus sit amet turpis dictum, fermentum risus vel, lacinia mi. Aliquam et mauris libero. Morbi augue leo, lacinia non posuere non, luctus vitae ligula. Curabitur blandit velit a nunc accumsan, a convallis nisi elementum. Ut nec condimentum mauris. In sit amet justo luctus ex ultrices laoreet at non arcu. Mauris suscipit elit vel rutrum elementum.

---
# Dedication

| Person     | Time  | Notes                                                    |
| :--------- | :---: | :------------------------------------------------------- |
| user       | xh xm | Lorem ipsum dolor sit amet, consectetur adipiscing elit. |
|            |       |                                                          |
| **Totals** |       |                                                          |
| user       | xh xm |                                                          |

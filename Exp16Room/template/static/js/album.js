window.onload = function () {
    images_location("waterfull", "box");
    function images_location(Parent, Children) {
        var parent = document.getElementById(Parent);//获取id为waterfull的元素
        var children = getChildElement(parent, Children);//通过一个封装函数来获取上述获取到的元素的所有符合条件的子元素，获得一个数组
        var imageWidth = children[0].offsetWidth;//因为在css中已经设定了固定宽度，所以只需要第一张图片的宽度。
        var cols = Math.floor(1250 / imageWidth);
        // 获取在固定宽度的情况下可以放下的列数。当然这里可以不用固定宽度，而使用用户浏览器的宽度document.documentElement.clientWidth。
        var hArr = [];
        for (var i = 0; i < children.length; i++) {
            if (i < cols) {
                hArr.push(children[i].offsetHeight);//将第一列中的图片高度数据存到hArr数组中
            } else {
                var minH = Math.min.apply(null, hArr);//又有Math.min方法的参数必须是一个一个的数，故这里使用apply方法传入数组求得最小的高度
                var index = getMinhIndex(hArr, minH);//封装一个函数获得最小高度的图片所在列的索引
                children[i].style.position = "absolute";//使用绝对定位
                children[i].style.top = minH + "px";//注意：这里一定要有px这个单位，否则将会出错
                children[i].style.left = imageWidth * index + "px";//即left的值
                hArr[index] += children[i].offsetHeight;//将刚添加的那一列的offsetHeight值更新
            }

        }

    }
    function getChildElement(Parent, Children) {
        var childrenArr = [];
        var allChildren = Parent.getElementsByTagName("*");
        for (var i = 0; i < allChildren.length; i++) {
            if (allChildren[i].className == Children) {//注意：原生JavaScript中对于元素由className这个属性，即获取类名。
                childrenArr.push(allChildren[i]);
            }
        }
        return childrenArr;
    }
    function getMinhIndex(arr, val) {
        for (var i in arr) { //遍历arr数组中的每一个元素，其中i表示各元素的索引
            if (arr[i] == val) {
                return i;
            }
        }
    }
}

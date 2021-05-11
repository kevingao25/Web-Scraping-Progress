raw_params = """comment: 测试测试testing—
submit: 发表评论
comment_post_ID: 13
comment_parent: 0"""

params = dict([line.split(": ",1) for line in raw_params.split("\n")])
print(params)



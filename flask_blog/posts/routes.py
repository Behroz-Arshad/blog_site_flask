from flask import Blueprint
from flask_login import current_user, login_required
from flask_blog.posts.forms import PostForm
from flask_blog.models import Post
from flask_blog import db
from flask import render_template, flash, redirect, url_for, request, abort

posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user = current_user
        post = Post(title=title, content=content, author=user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))

    return render_template('create_new_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route('/post/<int:post_id>')
@login_required
def post(post_id):
    specific_post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=specific_post.title, post=specific_post)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    specific_post = Post.query.get_or_404(post_id)
    if specific_post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        specific_post.title = form.title.data
        specific_post.content = form.content.data
        db.session.commit()
        flash('Updated successfully')
        return render_template('post.html', post=specific_post, post_id=specific_post.id)
    elif request.method == 'GET':
        form.title.data = specific_post.title
        form.content.data = specific_post.content
    return render_template('create_new_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route('/delete_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Deleted successfully', 'success')
    return redirect(url_for('main.home'))

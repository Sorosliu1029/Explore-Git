from IPython.display import display, HTML
import subprocess
import shlex

def display_tree(tree_sha, base_path, width):
    tree_content = subprocess.run(shlex.split(f'git -C {base_path} cat-file -p {tree_sha}'), capture_output=True, encoding='utf-8').stdout
    blobs = [e.split() for e in tree_content.strip().split('\n')]

    with open(f'tree{len(blobs)}.svg', 'rt', encoding='utf-8') as f:
        svg = f.read()
    
    svg = svg.replace('tree_sha', tree_sha[:7])
        
    for idx, blob in enumerate(blobs, start=1):
        blob_sha, filename = blob[2:4]

        svg = svg.replace(f'blob_sha_{idx}', blob_sha[:7])
        svg = svg.replace(f'filename_{idx}', filename)

        content = subprocess.run(shlex.split(f'git -C {base_path} cat-file -p {blob_sha}'), capture_output=True, encoding='utf-8').stdout
        svg  = svg.replace(f'content_{idx}', content)

    display(HTML(f'<div style="width: {width}">' + svg + '</div>'))

def display_general(base_path, width):
    with open(f'general.svg', 'rt', encoding='utf-8') as f:
        svg = f.read()

    with open(f'{base_path}/.git/HEAD', 'rt', encoding='utf-8') as f:
        head = f.read().split()[1]
    svg = svg.replace('refs/heads/head', head)

    with open(f'{base_path}/.git/{head}', 'rt', encoding='utf-8') as f:
        commit3_sha = f.read()
    svg = svg.replace('commit_sha_3', commit3_sha[:7])
    commit_3_msg = subprocess.run(shlex.split(f'git -C {base_path} log -1 --pretty=%B {commit3_sha}'), capture_output=True, encoding='utf-8').stdout.strip()
    svg = svg.replace('commit_msg_3', commit_3_msg)

    commit2_sha = subprocess.run(shlex.split(f'git -C {base_path} rev-parse HEAD~1'), capture_output=True, encoding='utf-8').stdout.strip()
    svg = svg.replace('commit_sha_2', commit2_sha[:7])
    commit_2_msg = subprocess.run(shlex.split(f'git -C {base_path} log -1 --pretty=%B {commit2_sha}'), capture_output=True, encoding='utf-8').stdout.strip()
    svg = svg.replace('commit_msg_2', commit_2_msg)

    commit1_sha = subprocess.run(shlex.split(f'git -C {base_path} rev-parse HEAD~2'), capture_output=True, encoding='utf-8').stdout.strip()
    svg = svg.replace('commit_sha_1', commit1_sha[:7])
    commit_1_msg = subprocess.run(shlex.split(f'git -C {base_path} log -1 --pretty=%B {commit1_sha}'), capture_output=True, encoding='utf-8').stdout.strip()
    svg = svg.replace('commit_msg_1', commit_1_msg)

    tree3_sha = subprocess.run(shlex.split(f'git -C {base_path} rev-parse {commit3_sha}^{{tree}}'), capture_output=True, encoding='utf-8').stdout.strip()
    svg = svg.replace('tree_sha_3', tree3_sha[:7])

    tree2_sha = subprocess.run(shlex.split(f'git -C {base_path} rev-parse {commit2_sha}^{{tree}}'), capture_output=True, encoding='utf-8').stdout.strip()
    svg = svg.replace('tree_sha_2', tree2_sha[:7])

    tree1_sha = subprocess.run(shlex.split(f'git -C {base_path} rev-parse {commit1_sha}^{{tree}}'), capture_output=True, encoding='utf-8').stdout.strip()
    svg = svg.replace('tree_sha_1', tree1_sha[:7])

    tree1_content = subprocess.run(shlex.split(f'git -C {base_path} cat-file -p {tree1_sha}'), capture_output=True, encoding='utf-8').stdout.strip()
    blob1 = [e.split() for e in tree1_content.strip().split('\n')][0]

    tree2_content = subprocess.run(shlex.split(f'git -C {base_path} cat-file -p {tree2_sha}'), capture_output=True, encoding='utf-8').stdout.strip()
    blob2 = [e.split() for e in tree2_content.strip().split('\n') if blob1[2] not in e][0]

    tree3_content = subprocess.run(shlex.split(f'git -C {base_path} cat-file -p {tree3_sha}'), capture_output=True, encoding='utf-8').stdout.strip()
    blob3 = [e.split() for e in tree3_content.strip().split('\n') if blob1[2] not in e and blob2[2] not in e][0]

    svg = svg.replace('blob_sha_1', blob1[2][:7])
    content1 = subprocess.run(shlex.split(f'git -C {base_path} cat-file -p {blob1[2]}'), capture_output=True, encoding='utf-8').stdout.strip()
    svg = svg.replace('content_1', content1)

    svg = svg.replace('blob_sha_2', blob2[2][:7])
    content2 = subprocess.run(shlex.split(f'git -C {base_path} cat-file -p {blob2[2]}'), capture_output=True, encoding='utf-8').stdout.strip()
    svg = svg.replace('content_2', content2)

    svg = svg.replace('blob_sha_3', blob3[2][:7])
    content3 = subprocess.run(shlex.split(f'git -C {base_path} cat-file -p {blob3[2]}'), capture_output=True, encoding='utf-8').stdout.strip()
    svg = svg.replace('content_3', content3)

    svg = svg.replace('t1b1', blob1[3])
    svg = svg.replace('t2b1', blob1[3])
    svg = svg.replace('t2b2', blob2[3])
    svg = svg.replace('t3b2', blob2[3])
    svg = svg.replace('t3b3', blob3[3])

    display(HTML(f'<div style="width: {width}">' + svg + '</div>'))
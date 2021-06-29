#!/usr/bin/env python
# coding=UTF-8

import os
import sys
import re
import argparse
import pprint
import csv
import json

name_dict = {
    # In VNDB Character list order
    # Protagonists
    '羽咲': 'Hasaki',
    '卓司': 'Takuji',
    '皆守': 'Tomosane',
    '由岐': 'Yuki',
    'ざくろ': 'Zakuro',
    # Main Characters
    '彩名': 'Ayana',
    '希実香': 'Kimika',
    '鏡': 'Kagami',
    '司': 'Tsukasa',
    # Side Characters
    'めぐ': 'Megu',
    '飯沼': 'Iinuma',
    '美羽': 'Miu',
    '木村': 'Kimura',
    '聡子': 'Satoko',
    '清川': 'Senagawa',
    '明日美': 'Asumi',
    'マスター': 'Master',
    '水上': 'Minakami',
    '西村': 'Nishimura',
    '沼田': 'Numada',
    'リルル': 'Riruru',
    '瀬名川': 'Senagawa',
    '城山': 'Shiroyama',
    '潔': 'Kiyoshi',
    'やす子': 'Yasuko',
    # Makes an appearance
    '飯田': 'Iida',
    '浩夫': 'Hiroo',
    '亜由美': 'Ayumi',
    '琴美': 'Kotomi',
    '母親': 'Mother',
    '宇佐美': 'Usami',
    # Not on VNDB
    'アリス': 'Alice',
    '共同（司・鏡）': 'Kagami+Tsukasa',
    'うさぎ': 'Rabbit',
    '本': 'Book',
    'くま': 'Bear',
    'おっさん': 'Man',
    '女子校生': 'Female Student',
    '男子校生': 'Male Student',
    '教師': 'Teacher',
    'タレブさん': 'Taleb-san',
    '校内放送': 'Announcement',
    'おばさん': 'Woman',
    '生田': 'Ikuta',
    '川端': 'Kawabata',
    '田村': 'Tamura',
    '島田': 'Shimada',
    '時坂': 'Tokisaka',
    '不安': 'Anxiety',
    '明日美の父': 'Asumi\'s Dad',
    '明日美の母': 'Asumi\'s Mom',
    'おばちゃん': 'Older Woman',
    '男性の通行人': 'Male Pedestrian',
    '女性の通行人': 'Female Pedestrian',
    '会社員': 'Office Worker',
    '観衆': 'Onlookers',
    '男性店員': 'Male Staff',
    '年配の男性教師': 'Elderly Male Teacher',
    '女性教師': 'Female Teacher',
    '他校生徒': 'Student from Another School',
    '不良達': 'Delinquents',
    '神': 'God',
    '悪しき者': 'Evil Person',
    'オカマ': 'Faggot',
    '練習生': 'Dojo Student',
    '渡辺': 'Watanabe',
}

def get_fnames():
    ret = []
    for root, dir, file in os.walk('txt_scripts_jp'):
        for fname in file:
            ret.append(os.path.join(root, fname))
    return ret

def create_translation_csv(outname=''):
    total_lines = []
    fnames = get_fnames()
    #fnames = sorted(fnames, key=sort_func)
    for fname in fnames:
        with open(fname, encoding='utf8') as f:
            scriptline = f.readline()
            while scriptline:
                scriptline = f.readline()
                #re_line = re.sub(r'\<\d*\,\d*\,\d*\>', "", scriptline)
                #true_line = re_line.rstrip()

                new_line = scriptline.rstrip()
                if new_line.lower() not in files:
                    print(new_line)
                    total_lines.append((new_line, fname))

                #m = re.search(r'.*?>([^a-zA-Z].*)', scriptline)
                #if m is not None:
                #    jp_line = m.group(1)
                #    if jp_line not in name_dict.keys() and '#FFFFFF' not in jp_line and '6sakura' not in jp_line:  # TODO: Fix
                #        total_lines.append((jp_line, fname))
    print('Total number of lines: {}'.format(len(total_lines)))

    with open(outname, 'w', encoding='utf8') as csvfile:
        csvwriter = csv.writer(csvfile)
        for line, fname in total_lines:
            csvwriter.writerow([line, line, fname])

def create_translation_scripts():
    translation = []
    with open('translation.csv', 'r', encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            translation.append((row[0], row[1]))

    fnames = get_fnames()
    #fnames = sorted(fnames, key=sort_func)
    en_files = []
    idx = 0
    for fname in fnames:
        print(fname)
        prefix = ""
        #outname = os.path.join('txt_scripts_en', fname.split('/')[1].split('.')[0] + '.txt')
        fshort = os.path.split(fname)[1]
        outname = os.path.join('txt_scripts_en', os.path.splitext(fshort)[0] + '.txt')
        with open(outname, 'w', encoding='utf8') as en_f:
            with open(fname, 'r', encoding='utf8') as jp_f:
                jp_scriptline = jp_f.readline()
                en_f.write(jp_scriptline)
                while jp_scriptline:
                    jp_scriptline = jp_f.readline()

                    #jp_re_line = re.sub(r'\<\d*\,\d*\,\d*\>', "", jp_scriptline)
                    jp_newline = jp_scriptline.rstrip()

                    #p = re.search(r'\<\d*\,\d*\,\d*\>', jp_scriptline)
                    #if p != None:
                    #    prefix = p.group(0)
                    #else:
                    #    prefix = None

                    if jp_newline.lower() in files:
                        en_f.write(jp_newline)
                    else:
                        eng_newline = translation[idx][1]
                        en_f.write(eng_newline)
                        idx += 1
                    en_f.write("\n")

                    #    if prefix != None:
                    #        new_eng = translation[idx][1]
                    #        en_f.write(prefix + new_eng)
                    #        idx += 1
                    #        en_f.write("\n")


                    # if 'ruby' in jp_scriptline:
                    #     next_line = jp_f.readline()
                    #     endruby = jp_f.readline()
                    #     next_next_line = jp_f.readline()
                    #     jp_scriptline = next_line[:-3] + next_next_line[1:]
                    # if 'name' in jp_scriptline and '？？？' not in jp_scriptline:
                    #     m = re.search(r'^name={name="(.*)"},$', jp_scriptline)
                    #     name = m.group(1)
                    #     eng_line = 'name={{name="{}"}},\n'.format(name_dict[name])
                    #     en_f.write(eng_line)
                    #     continue
                    # m = re.search(r'^"(.*)",$', jp_scriptline)

                    #m = re.search(r'(.*?>)([^a-zA-Z].*)', jp_scriptline)
                    # if m.group(2) is not None:
                    #if m is not None:
                    #    jp_line = m.group(2)
                    #    if jp_line not in name_dict.keys() and '#FFFFFF' not in jp_line and '6sakura' not in jp_line:  # TODO: Fix
                    #        check_jp_line, new_eng_line = translation[idx]
                    #        new_eng_line = '{}: {}'.format(str(idx + 1), new_eng_line)  # For debugging
                    #        idx += 1
                    #        try:
                    #            assert jp_line == check_jp_line
                    #        except:
                    #            print(check_jp_line)
                    #            print(jp_line)
                    #            #1/0
                    #        eng_line = '{}{}\n'.format(m.group(1), new_eng_line)
                    #        en_f.write(eng_line)
                    #    if jp_line in name_dict.keys():
                    #        eng_line = '{}{}\n'.format(m.group(1), name_dict[m.group(2)])
                    #        en_f.write(eng_line)
                    #else:
                    #    en_f.write(jp_scriptline)

                    # try:
                    #     eng_line = '"{}",\n'.format(translation[m.group(1)])
                    #     en_f.write(eng_line)
                    #     # print('Replaced {} with {}'.format(scriptline, eng_line))
                    # except AttributeError:
                    #     en_f.write(jp_scriptline)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--make_csv', help='File to save empty translation csv', default='',
                        type=str)
    parser.add_argument('--make_translation_scripts', help='use translation.csv to rewrite scripts',
                        action='store_true', default=False)
    args = parser.parse_args()

    print('Arguments:\n{}\n'.format(' '.join(sys.argv[1:])))

    print('Config:')
    pprint.pprint(vars(args), depth=2, width=50)

    with open('files.json', encoding="utf8") as o:
        files = json.load(o)

    if args.make_csv:
        create_translation_csv(outname=args.make_csv)
    if args.make_translation_scripts:
        create_translation_scripts()
    # print_names()

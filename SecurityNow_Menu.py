import SecurityNow_Class
import DownloadURL


def main():
    sn = SecurityNow_Class.SecurityNow()
    i = input('Download To Episode: ')
    for ep in range(sn.get_next_ep(), int(i) + 1):
        print('Episode ' + str(sn.get_next_ep()) + ' download...', end='', flush=True)
        # print(sn.get_url_for_next_transcript())
        dw = DownloadURL.DownloadURL(sn.get_url_for_next_audio())
        if dw.download_save(sn.gen_filename_next()):
            print(DownloadURL.BColors.OKGREEN + 'Successful.' + DownloadURL.BColors.ENDC)
            sn.update_current()
            sn.write_log()
        else:
            print(DownloadURL.BColors.WARNING + 'Failed.' + DownloadURL.BColors.ENDC)

if __name__ == '__main__':
    main()

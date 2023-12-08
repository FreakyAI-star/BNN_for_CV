class Path(object):
    @staticmethod
    def db_dir(database):
        if database == 'ucf101':
            # folder that contains class labels
            root_dir = '/workspace/pytorch-video-recognition/UCF-101'

            # Save preprocess data into output_dir
            output_dir = '/workspace/pytorch-video-recognition/UCF_preprocessed'

            return root_dir, output_dir
        elif database == 'hmdb51':
            # folder that contains class labels
            root_dir = '/workspace/pytorch-video-recognition/HMDB51'

            # Save preprocess data into output_dir
            output_dir = '/workspace/pytorch-video-recognition/HMDB_RGB'

            return root_dir, output_dir
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError

    @staticmethod
    def model_dir():
        return '/workspace/pytorch-video-recognition/pretrained/c3d-pretrained.pth'

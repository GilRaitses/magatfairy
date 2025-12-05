function info = getInfo(obj)
    % getInfo - Return experiment information struct
    %
    % Returns a struct with:
    %   num_tracks - Number of tracks in the experiment
    %   num_frames - Total number of frames in the experiment
    %
    % Usage:
    %   info = app.getInfo();
    %   num_tracks = info.num_tracks;
    %   num_frames = info.num_frames;
    
    info = struct();
    info.num_tracks = obj.num_tracks;
    info.num_frames = obj.num_frames;
end


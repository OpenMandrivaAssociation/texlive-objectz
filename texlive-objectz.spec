# revision 19389
# category Package
# catalog-ctan /macros/latex/contrib/objectz
# catalog-date 2006-12-30 22:14:40 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-objectz
Version:	20061230
Release:	1
Summary:	Macros for typesetting Object Z
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/objectz
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/objectz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/objectz.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/objectz.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package will typeset both Z and Object-Z specifications; it
develops the original zed package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/objectz/oz.sty
%doc %{_texmfdistdir}/doc/latex/objectz/catalog
%doc %{_texmfdistdir}/doc/latex/objectz/makefile
%doc %{_texmfdistdir}/doc/latex/objectz/manifest
%doc %{_texmfdistdir}/doc/latex/objectz/ozguide.pdf
%doc %{_texmfdistdir}/doc/latex/objectz/ozguide.tex
%doc %{_texmfdistdir}/doc/latex/objectz/oztest.tex
%doc %{_texmfdistdir}/doc/latex/objectz/readme
#- source
%doc %{_texmfdistdir}/source/latex/objectz/oz.dtx
%doc %{_texmfdistdir}/source/latex/objectz/oz.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}